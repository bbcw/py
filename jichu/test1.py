#coding:utf-8

def trapezoid_area(base_up, base_down, height=3):
    return 1/2 * (base_up + base_down) * height

# base_up = 1
# base_down = 2
# height = 3
#print(trapezoid_area(height, base_down, base_up))
print(trapezoid_area(1,2,5))
print('   *','  * *',' * * *','   |  ',sep = '\n')