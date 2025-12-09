import re
import urllib.request
import datetime

# opens file where you put each moksha url in a new line and turns it
# into an array
f = open("moksha_URLS")
raw_urls = f.read()
f.close()
url_array =raw_urls.split()

# regex for finding market name + queue position
pattern1 = r"(?<=QueuePosition<\/th><td>)\d+"
pattern2 = r"(?<=SubmissionStatus-)\w+"

# opens/creates output file for results w/timestamp (appends, so you can
# see how little you moved from the last time you checked!)
o = open(file="moksha_output",mode="a+")
o.write(f"{datetime.datetime.now()}\n{"-"*25}\n")

# inits for the core loop
i = 0
market = ""
queue_num = ""

for i in range(len(url_array)):
    # opens URL and saves as string
    fp = urllib.request.urlopen(url_array[i])
    my_bytes = fp.read()
    html_str = my_bytes.decode("utf8")
    fp.close()
    # strips out whitespace
    html_str =html_str.strip()
    html_str =html_str.replace(" ","")
    html_str =html_str.replace("\t","")
    html_str =html_str.replace("\n","")
    # run regex and output results to terminal + file
    market = str(re.findall(pattern2,html_str))
    queue_num = str(re.findall(pattern1,html_str))
    print(f"{market[2:-2]:<20}{queue_num[2:-2]:>10}")
    o.write(f"{market[2:-2]:<20}{queue_num[2:-2]:>10}\n")

# closes output file
o.close()