# Omkar Patil, 2024 
# See README 

import os 
from urllib import urlopen 
from bs4 import BeautifulSoup
import re 

# URL of wikipedia page 
source = urlopen('https://en.wikipedia.org/wiki/Python_(programming_language)').read()