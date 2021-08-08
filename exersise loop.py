# 3 امثلة دول بيطبعو نفس النتيجة
'''
print('number   square')
for i in range(1,11):
    print(i,'\t',i*i)
-----------------------------
x=0
while x<11:
    print(x,'\t',x*x)
    x+=1
-----------------------------
start=int(input('enter the start num: '))
end=int(input('where should i go :'))
for i in range(start,end+1):
    print(i,'\t',i*i)
    
------------------------------
rows=int(input('how many rows :'))
cols=int(input('how many cols :'))
for r in range (rows):
    for c in range (cols):
        print('*',end='')# end='' عشان اطبعهم جمب بعض
    print()# عشان ينزل سطر او اسيب مصافة بين كل صف
------------------------------
x=input('enter your num:')
for i in range (1,9):
    print(i*x)
-----------------------------    
#حل اخر
size=8
for r in range(8):
    for c in range (r):
        print('*',end='')
    print()
  # thanks this looop finshed
'''
x=input('enter your num:')
for i in range (1,9):
    print(i*x)
    

    
