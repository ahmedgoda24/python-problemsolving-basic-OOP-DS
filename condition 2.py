'''
x=200
if x==100:
    print('x=100')
elif x==200:
    print('x=200')
    if x>100:
        print('x > 100')
    elif x<300:
        print('x < 300')
elif x==250:
    print("good")
else:
    print("close")
'''
#------------------------------------------------#
'''
x=200
if x==100:
    print('x=100')
elif x==200:
    print('x=200')
    if x>100:
        print('x > 100')
    if x<300:
        print('x < 300')
elif x==250:
    print("good")
else:
    print("close")
'''
#_______________________________________________________#
'''
players={'goda':2,'ahmed':1}
if 'goda' in players:
    print("found")
'''
#__________________________________________________#
x=int(input("enter number:"))
if x>=65 and x<75:
    print("good")
elif x>=75 and x<85:
    print("very good")
elif x>=85 and x<=100:
    print("exellant")
else :
    print("sucess")
    
