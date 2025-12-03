import re
import urllib.request

# opens file where you put each moksha url in a new line and turns it into an array
f = open("moksha_URLS")
raw_urls = f.read()
f.close()
url_array =raw_urls.split()

# regex for finding market name + queue position
pattern1 = r"(?<=QueuePosition<\/th><td>)\d+"
pattern2 = r"(?<=SubmissionStatus-)\w+"

i = 0

for i in range(len(url_array)):
    # opens URL and saves to html_str
    fp = urllib.request.urlopen(url_array[i])
    my_bytes = fp.read()
    html_str = my_bytes.decode("utf8")
    fp.close()
    # strips out whitespace to make one big ol str
    html_str =html_str.strip()
    html_str =html_str.replace(" ","")
    html_str =html_str.replace("\t","")
    html_str =html_str.replace("\n","")
    print(f"{re.findall(pattern2,html_str)}\t\t {re.findall(pattern1,html_str)}")