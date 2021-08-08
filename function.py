'''
def summ(x,y):
    print(x+y)
    return
summ(5,5)
#--------------------

summ=lamda x,y:x+y
print("totl:",summ(20,20))
#-------------------------

def summ(x,y):
    z=x+y
    return z
a=summ(5,5)
print(a)    
#---------------------

def printme(arg,*vartuple):
    print('output')
    print(arg,vartuple)
    return
printme(10,50,60,70)
#----------------------------------

def printme(arg,*vartuple):
    print('output')
    print(arg)
    for var in vartuple:
        print(var)
        return

printme(10)
printme(20,30,40)
#----------------------------------

def printme(arg,*vartuple):
    print('output')
    print("arg is:",arg)
    print("vartuple is :",vartuple)
    for var in vartuple:
        print(var)
    return
printme(10,50,60,70)
#------------------------------
'''

def printme(arg,*vartuple):
    print('output')
    #print(arg)
    #print(vartuple)
    res = arg
    for var in vartuple:
        res = res +var
        
    print(res)
    

printme(10,20,30,40)















