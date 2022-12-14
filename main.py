import os
import requests
from bs4 import BeautifulSoup

base_url = "https://animego.org/"

base_req = requests.get(base_url)

with open('page.txt', 'w') as f:
    f.write(base_req.text)
    #print(req.text, file=f)


base_page = BeautifulSoup(base_req.text)

links = []

with open('links.txt', 'w') as f:
    for link in base_page.findAll('a'):
        link_text= link.get('href')
        if("https:" in link_text):
            f.write(link_text+"\n")
            links.append(link_text)
        #print(link.get('href'))



print(f"link \"{base_url}\" --------")
print("\tpage content saved in file:", "page.txt")
print("\tlinks found:", len(links))
print("\tlinks saved in file:", "links.txt")


