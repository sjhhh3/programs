import random
import urllib.request

def download_web_image(url):
    name = random.randrange(1,1000)
    full_name = str(name) + ".jpg"
    urllib.request.urlretrieve(url,full_name)

download_web_image("https://i.h2.pdim.gs/3459966f6e12c3f61e596278e5af4b54.png")