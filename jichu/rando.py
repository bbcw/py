#coding:utf-8

import random
point1 = random.randrange(1,6)
point2 = random.randrange(1,6)
point3 = random.randrange(1,6)

point= point1 + point2 + point3

# def panduan():

print(point)
print('<<<<< GAME STARTS! >>>>>')
num = input('Big or Small: ')
if 11 <= point <= 18:
    if num == 'Big':
        print('The points are', [point1,point2,point3] ,'You Wing!')
    elif num ==  'Small':
        print('The points are', [point1, point2, point3], 'You Lose!')
    else:
        print('Please enter the correct options!')
    # panduan()
elif 3<= point <= 10:
    if num == 'Big':
        print('The points are', [point1,point2,point3] ,'You Losw!')
    elif num == 'Small':
        print('The points are', [point1, point2, point3], 'You Wing!')
    else:
        print('Please enter the correct options!')
