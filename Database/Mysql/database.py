"""
author:lightfish
Time:2018.11.8
note:向数据库中灵活插入数据，字典的方式
"""
f = open(r'E:\python_project\weixin\血小板.csv')
df = pd.read_csv(f)
print(np.random.choice(df['author']))

s = '2016210'
def input_data():
    for _ in range(15):
        data={
            'id': s+str(np.random.choice(np.arange(405068,406666))),
            'name': np.random.choice(df['author']),
            'age': np.random.randint(16,80)
        }
        insert_to_MySQL(data)



def insert_to_MySQL(data):
    table = 'students'
    keys = ','.join(data.keys())
    values = ','.join(['%s'] * len(data))
    # on duplicate key update
    sql = 'INSERT INTO {table}({keys}) VALUES ({values}) ON DUPLICATE KEY UPDATE'.format(table=table, keys=keys,
                                                                                         values=values)
    update = ','.join([' {key}=%s'.format(key=key) for key in data.keys()])
    sql += update

    try:
        if cursor.execute(sql, tuple(data.values()) * 2):
            print('Sucessfull insert...')
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

input_data()
