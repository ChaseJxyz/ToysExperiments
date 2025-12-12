import re
import urllib.request
import datetime

# opens file with 1 moksha url per line + converts into
# array
f = open("moksha_URLS")
raw_urls = f.read()
f.close()
url_array = raw_urls.split()

# regex for finding market name + queue position + sub status
queue_pattern = r"(?<=QueuePosition<\/th><td>)\d+"
market_pattern = r"(?<=SubmissionStatus-)\w+"
status_pattern = r"(?<=<th>Status<\/th><td>)\w+"

# silly dict for prettifying results
# feel free to remove the emoji
results = {
    # i only have rejected/accepted urls to test so idk if
    # the others work yet
    "rejected": "Rejected 😿",
    "accepted": "🎉Accepted🎉",
    "revisionrequested": "Revision Requested 🙀",
    "withdrawn": "Withdrawn 🐈‍⬛",
    "inprogress": "In Progress 😺",
}

"""
Additional moksha statuses (that are probably backend-only, but storing
here in case they might be of use later):
Open, Closed, Archived, Claimed, File Error, Needs Second Opinion,
Not recommended, Recommended, Unclaimed
"""


# turns array into string
def delister(list):
    return "".join(list)


# puts whitespaces back into market name
# it a'int perfect but it's close
def despacer(name):
    return re.sub(r"(?<=\w)([A-Z])", r" \1", name)


# opens/creates output file for results w/timestamp (appends, so you can
# see how little you moved from the last time you checked!)
o = open(file="moksha_output", mode="a+")
o.write(f"{datetime.datetime.now()}\n{'-' * 25}\n")

# inits for the core loop
i = 0
market = ""
sub_status = ""

for i in range(len(url_array)):
    # opens/closes URL and saves as string
    fp = urllib.request.urlopen(url_array[i])
    my_bytes = fp.read()
    html_str = my_bytes.decode("utf8")
    fp.close()
    # strips out whitespace from webpage
    html_str = html_str.strip()
    html_str = html_str.replace(" ", "")
    html_str = html_str.replace("\t", "")
    html_str = html_str.replace("\n", "")
    # find/save/format market name
    market = re.findall(market_pattern, html_str)
    market = delister(market)
    market = despacer(market)
    # looks for queue position
    sub_status = re.findall(queue_pattern, html_str)
    # runs if no digits (i.e. closed sub or market doesn't share positions)
    # find/save/format sub status
    if sub_status == []:
        sub_status = object = re.findall(status_pattern, html_str)
        sub_status = delister(sub_status)
        sub_status = results[sub_status]
    else:
        sub_status = delister(sub_status)
    # print results to terminal
    print(f"{market:<20}{sub_status:>10}")
    # writes results to output file
    o.write(f"{market:<20}{sub_status:>10}\n")

# closes output file
o.close()
