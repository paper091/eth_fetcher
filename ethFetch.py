import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://etherscan.io/tx/0xe48a42dc70619677d1db41663896a960ca55c659ad468f705bcd3c7475b11df4'
headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
response = requests.get(url, headers= headers)
# Check if the request was successful
   
if response.status_code != 200:
    print("Failed to fetch the website.")
    exit()

# Parse the HTML content with BeautifulSoup
html_content = response.content
soup = BeautifulSoup(html_content, 'html.parser')

key = []
val = []
skip = ["Sponsored:", "", " "]
c = 0

container = soup.find("div", id="ContentPlaceHolder1_maintable")
for div in container.find_all("div", class_="row mb-4"):
    for i in div:
        t = i.text.strip()
        if(t in skip):
            continue

        if(c == 0):
            key.append(t)
            c = 1
        else:
            val.append(t)
            c = 0

# print(len(key))
# print(len(val))
# print(key)
# print(val)

data = { 
    'Key': key,
    'Val': val
}
df = pd.DataFrame(data)
print(df)
# div2 = soup.find_all("div", class_="p-5 pb-0")

# print(div1)
# print(div2)