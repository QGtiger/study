import requests
from bs4 import BeautifulSoup
import urllib.request
import pytesseract
from PIL import Image

img=Image.open(r'D:\360极速浏览器下载\3.png')
code=pytesseract.image_to_string(img,lang='chi_sim')
print(code)
list=code.split('\n\n')

question=list[0]
answer1=list[1]
answer2=list[2]
answer3=list[3]

base_url='https://zhidao.baidu.com/search?ct=17&pn=0&tn=ikaslist&rn=10&fr=wwwt&word={}'
questionParm=urllib.request.quote(question)

url=base_url.format(questionParm)
print(url)
html=requests.get(url)
soup=BeautifulSoup(html.content,'html.parser')
items=soup.find_all('dl')
count1,count2,count3=0,0,0
for i in items:
    result=i.find('dd','dd answer')
    '''
    print(result.get_text().count('岛妹'),end='\n\n')
    '''
    if result is not None:
        count1+=result.get_text().count(answer1.replace(' ',''))
        count2+=result.get_text().count(answer2.replace(' ',''))
        count3+=result.get_text().count(answer3.replace(' ',''))
print('答案中A出现的次数:'+str(count1))
print('答案中B出现的次数:'+str(count2))
print('答案中C出现的次数:'+str(count3))
list1=[count1,count2,count3]
dict={0:'A',1:'B',2:'C'}
print('所以推荐答案是'+str(dict[list1.index(max(list1))]))



