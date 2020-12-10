import urllib.request, urllib.parse, urllib.error
from bs4 import Beautifulsoup
import ssl

ctx = ssl.creat_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE

url = input('Enter - ')
html = urllib.request.urlopen(url, context=ctx).read()
soup = Beautifulsoup(html, 'html.parser')

tags = soup('a')
for tag in tags:
    print(tag.get(href, None))
