import urllib.request
"""
res = urllib.request.urlopen('http://placekitten.com/g/200/200')
cat_img=res.read()
with open('cat_img.jpg','wb')as f:
    f.write(cat_img)
"""
res = urllib.request.urlopen('http://www.fishc.com')
text=res.read()
print(type(text))
text=text.decode('utf-8')
#print(type(text))
#print(text)
with open('test.txt','w')as f:
    f.write(text)
