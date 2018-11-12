import pandas as pd

data={
    'name':['辰东','辰战','萧薰儿'],
    'age':[18,44,16],
    'gender':['男','男','女']
}
df = pd.DataFrame(data)
print(df)
#df.to_csv(r'E:\python_project\weather\test.csv',index=False)

f = open(r'E:\python_project\weather\蚁人2影评.xlsx','rb')
df = pd.read_excel(f)
print(df)
