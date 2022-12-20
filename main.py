import os
import requests
from bs4 import BeautifulSoup
import web_parse_a as wp_a

base_url = "https://animego.org/" #only for demonstration

os.system("clear")

print("< WEB PARSER >\n")
print("> web parse starting...")
print(f"> base point -> {base_url}\n")

#old method
#tree = wbt.web_tree(base_url)
#tree.generate(2)



#base_page_urls = wp_a.parse_page_for_urls(base_url)

#print("> found ->",len(base_page_urls))
#for url in base_page_urls:
#    print(" ->", url)

wp_a.reset_all()

wp_a.recursive_parse(base_url, depth=2)

#output
c=0
for d in wp_a.web_data:
    print(c,f"\"{d[0]}\"", d[1])
    c+=1
print("> all_urls length ->", len(wp_a.all_urls))
print("> web_data length ->", len(wp_a.web_data))