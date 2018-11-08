def input_data():
    for _ in range(15):
        data={
            'id': input('输入学号：'),
            'name': input('输入名字：'),
            'age': int(input('输入年龄：'))
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
        cursor.execute(sql, tuple(data.values()) * 2)
        print('Sucessfull insert...')
        db.commit()
    except Exception as e:
        print(e)
        db.rollback()

input_data()