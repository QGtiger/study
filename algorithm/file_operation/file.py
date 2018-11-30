
def file_add():
    with open('3.txt','w') as f:
        for line in open('1.txt','r'):
            f.write(line)
        f.flush()
        for line in open('2.txt','r'):
            f.write(line)
        f.flush()

if __name__ == '__main__':
    print('1.txt和2.txt合并请输入1')
    while True:
        n = input('请输入指令: ')
        if n == '1':
            file_add()
