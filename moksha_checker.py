import re
import urllib.request
import datetime
from html import unescape

# nice formatting for output
table_width = 35
separator = "-" * table_width

# opens file with 1 moksha url per line + converts into array
try:
    f = open("moksha_URLS")
    raw_urls = f.read()
    f.close()
    url_array = raw_urls.split()
except FileNotFoundError:
    print("Please make a URL file! Otherwise this has nothing to do :)")
    quit()

# regex for finding market name + queue position + sub status
queue_pattern = r"(?<=QueuePosition<\/th><td>)\d+"
market_pattern = r"(?<=SubmissionStatus-)(.*?)\|"
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


# read all old entries and turn into array
try:
    o = open(file="moksha_output", mode="r")
    previous_entries = o.readlines()
    o.close()
except FileNotFoundError:
    print("No history found")
    previous_entries = []


# finds last instance script ran + saves results into list
last_checked_index = 0
last_checked_markets = []

for index, element in reversed(list(enumerate(previous_entries))):
    if element[0:3] == "---":
        last_checked_index = index + 1
        break

for element in range(last_checked_index, len(previous_entries)):
    temp = previous_entries[element]
    temp = temp.strip("\n")
    temp = re.split(r'[" "]{2,}', temp)
    if temp[1][1] in [0 - 9]:
        temp[1] = int(temp[1])
    last_checked_markets.append(temp)


# converts list into dict cause i couldnt get it to work otherwise
prev_dict = {}

x = 0
for x in range(0, len(last_checked_markets)):
    prev_dict[last_checked_markets[x][0]] = last_checked_markets[x][1]


# opens/creates output file for results w/timestamp
o = open(file="moksha_output", mode="a+")
o.write(f"{datetime.datetime.now()}\n{separator}\n")


# inits for the core loop
i = 0
x = 0
market = ""
sub_status = ""
difference = 0

for i in range(len(url_array)):
    difference = 0
    x = 0
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
    if "&" in market:
        market = unescape(market)
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
        if ord(sub_status[0]) in range(48, 60):
            sub_status = int(sub_status)
    if market in prev_dict:
        if isinstance(sub_status, int):
            difference = int(prev_dict[market]) - int(sub_status)
    # print results to terminal
    print(f"{market:<25}{sub_status:>10}")
    if difference != 0:
        print(f"{(-1 * difference):>35}")
    # writes results to output file
    o.write(f"{market:<25}{sub_status:>10}\n")
    if difference != 0:
        o.write(f"{(-1 * difference):>35}\n")

# closes output file
o.close()
