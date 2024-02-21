#pip install requests
#pip install selectolax
import requests
from selectolax.parser import HTMLParser

title = "Ai"

url = f"https://scholar.google.com/scholar?as_ylo=2024&q={title}&hl=fa&as_sdt=2023"
resp = requests.get(url)
parser = HTMLParser(resp.content)
for title in parser.css('.gs_r'):
    if title.css_first('.gs_ri h3') != None:
        print(title.css_first('.gs_ri h3 a').text())
        print(title.css_first('.gs_rs').text())
    if title.css_first('.gs_ggs a') != None:
        print(title.css_first('.gs_ggs a').attrs.get('href'))
    print('_____________________________By Ali Jahani_______________________________')
