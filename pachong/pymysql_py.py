import pymysql

db=pymysql.connect(host='localhost',user='root',password='',port=3306,db='python')
cursor=db.cursor()
data={
    'num':1,
    'name':'QGnb',
    'score':'9.9'
    }
table='maoyantop100'
keys=','.join(data.keys())
values=','.join(['%s']*len(data))
sql='insert into {table} ({keys}) values({values}) on duplicate key update'.format(table=table,keys=keys,values=values)
update=','.join([' {key} = %s'.format(key=key) for key in data])
sql+=update
try:
    if cursor.execute(sql,tuple(data.values())*2):
        print('Successful！')
        db.commit()
except:
    print("Failed")
    db.rollback()
db.close()
