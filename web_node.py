import os
import requests
from bs4 import BeautifulSoup
import math

def get_links(bs_page):
    links = set()
    for link in bs_page.findAll('a'):
        link_text= link.get('href')
        if("https" in link_text):
            #f.write(link_text+"\n")
            links.add(link_text)
    print("$$$", len(list(links)))
    return links

class web_tree:
    def __init__(self, base_url):
        self.all_links = set(base_url)
        self.base_node = web_node(base_url)
        self.depth = 0

    def generate(self, depth):
        self.depth = depth
        self.base_node.generate(self.depth, self.all_links)

class web_node:
    def __init__(self, url):
        self.url = url
        self.depth = 0
        self.page = requests.get(url)
        self.bs_page = BeautifulSoup(self.page.text)
        self.links = set()
        self.child_nodes = set()
        self.weight_scale = 1
        self.weight = 1


    def generate(self, depth, all_links):
        
        self.depth = depth
        
        self.links = get_links(self.bs_page)
        self.weight = self.weight_scale/(1+math.log(len(self.links)+1)) 
        
        self.info() 
        
        if(self.depth > 0):
            for next_url in self.links:
                if not (next_url in all_links):
                    new_node = web_node(next_url)
                    new_node.generate(self.depth - 1, all_links)
                    self.child_nodes.add(new_node)
                    
            #for child_node in self.child_nodes:

        all_links.union(self.links)

    
    def info(self):
        print("  "*(3-self.depth)+"\__"+f" | links - {len(list(self.links))} | url -> {self.url}")
        
        