'''
f=0
print(f)  #global f

def fun():
    f=5
    print(f)  #local f

fun()
print(f) #global f
______________________________
f=0
print(f)  

def fun():
    global f
    f=5
    print(f)
fun()
print(f)
'''
