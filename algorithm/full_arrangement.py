import itertools
def permutation(list, start, end):
    global count
    global list2
    if start == end:
        count+=1
        print(''.join(list))
        if not ''.join(list) in list2:
            list2.append(''.join(list))
    else:
        for j in range(start,end+1):
            list[j],list[start]=list[start],list[j]
            permutation(list,start+1,end)
            list[j], list[start] = list[start], list[j]

if __name__=='__main__':
    str=input('请输入您要进行全排列的字符串：')
    count=0
    list2=[]
    print('list的排序：')
    permutation(list(str),0,len(str)-1)

    print('总共有%d中排序方式' % count)
    print('list2:',list2)
    print('排除重复，真实的排序方式个数为',len(list2))

    #itertools模块现成的全排列：

    for i in itertools.permutations('122', 3):
        print(''.join(i))