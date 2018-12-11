import jieba.analyse
import matplotlib.pyplot as plt
from wordcloud import WordCloud,STOPWORDS,ImageColorGenerator
import requests
import numpy as np
from PIL import Image


content = requests.get('http://39.108.219.55:8080/bkcontent?url=https://www.qu.la/book/746/10632452.html').text
tags = jieba.analyse.extract_tags(
    content, topK=40, allowPOS=(
        'ns', 'n', 'vn', 'v', 'nr'))
contents = ' '.join(tags)
#读取图片
background_image = np.array(Image.open('5.JPG'))
#提取背景图片的颜色
img_color = ImageColorGenerator(background_image)
#设置停止词
stopword = set(STOPWORDS)
wc = WordCloud(
    mask=background_image,
    font_path=r'C:\Windows\font\kaiu.ttf',
    background_color='white',
    width=800,
    height=400,
    margin=2,
    max_words=100,
    min_font_size=15,
    random_state=100,
    repeat=False
)
wc.generate_from_text(contents) # 等价于wc.gernerate(contents)
# #根据图片色设置背景色
# wc.recolor(color_func=img_color)
wc.to_file('yoona.jpg')
#显示图片
plt.imshow(wc)
plt.axis('off')
plt.show()
