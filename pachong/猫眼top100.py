import requests
from bs4 import BeautifulSoup
import pymysql

print("连接到mysql服务器...")
db= pymysql.connect(
        host='localhost',
        port = 3306,
        user='root',
        passwd='',
        db ='python',
        )
print("连接成功！")
# 数据的游标
cursor = db.cursor()
# 选择数据库
#cursor.execute("use test")
#计数
num = 0

# 网页请求头
headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.89 Safari/537.36 OPR/49.0.2725.47'}
url = "http://maoyan.com/board/4?offset="

for i in range(0, 100, 10):  # 从0开始，每次增加10，到100结束，不包括100
    url = "http://maoyan.com/board/4?offset=" + str(i)
    # 发送get请求
    r = requests.get(url, headers=headers)
    # 获取文本
    content = r.text
    soup = BeautifulSoup(content, 'html.parser')

    div_name = soup.find_all(class_='name')  # 找出所有电影的名字
    div_star = soup.find_all(class_='star')  # 找出所有电影的主演
    div_time = soup.find_all(class_='releasetime')  # 找出所有电影的上映时间
    div_score = soup.find_all(class_='score')  # 找出所有电影的评分

    long = len(div_name)

    for i in range(0, long):
        num = num + 1
        number = str(num)
        name = div_name[i].get_text()
        actor = div_star[i].get_text()
        date = div_time[i].get_text()
        score = div_score[i].get_text()
        #插入数据
        insert_name = "insert into maoyantop(num,name,actor,date,score) values(%s,%s,%s,%s,%s)"
        data = (number,name.strip(),actor,date,score)
        cursor.execute(insert_name, data)
        db.commit()
        print("第 "+ str(num) +" 条插入完成")
