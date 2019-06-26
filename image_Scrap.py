from bs4 import BeautifulSoup
import requests
handle = raw_input('Input your account name on Twitter: ') 
temp = requests.get('https://twitter.com/'+handle)
bs = BeautifulSoup(temp.text,'lxml')

pic=bs.find_all("img",{"class": "ProfileAvatar-image "})
url=pic[0]['src']

from PIL import Image
import requests
from io import BytesIO

response = requests.get(url)
img = Image.open(BytesIO(response.content))
img.show()
