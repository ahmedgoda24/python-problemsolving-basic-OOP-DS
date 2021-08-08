''' nested loop
x=0
while x<5:
    y=0
    print(x+1,"interation")
    while y<3:
        print("x=",x,"y=",y)
        y+=1
    x+=1
'''


for x in 'python':
    print(x)
    print('--------------')
    for y in 'ahmed':
        print(y)
        
#نفس المثال باستخدام while وfor
'''
a=0
while a<4:
    a+=1
    b=0
    while b<4:
        b+=1
        print(a,b)
'''

'''
for a in range(1,5):
    for b in range (1,5):
        print(a,b)
        
'''
