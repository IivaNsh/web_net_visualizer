import os
import requests
from bs4 import BeautifulSoup
import web_node as wbt

base_url = "https://animego.org/"

print("...")

tree = wbt.web_tree(base_url)
tree.generate(1)