#coding:utf-8
def create_txt(num):
    path = 'E:/siren/python/txt/'
    name = path + num + '.txt'
    file = open(name,'w')
    file.write(' ')
    file.close()
    print('Done!')

for i in range(1,11):
    create_txt(str(i))
    '''需要注意的地方，必须要把i转换成str类型，否则报typeerror
    TypeError: Can't convert 'int' object to str implicitly'''