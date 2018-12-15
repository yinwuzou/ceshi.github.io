import urllib.request
url = 'http://placekitten.com/100/200'
respones = urllib.request.urlopen(url)
cat_img = respones.read()
with open('cat_100_200.jpg','wb')as f:
        f.write(cat_img)