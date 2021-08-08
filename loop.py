'''
x=-1
for n in[10,20,30,55,66,99]:
    if n>x:
        x=n
    print(x,n)
    print(x)
'''

'''
def area(h,w):
    print(h*w)
    
h=float(input("enter the heigh:"))
w=float(input("enter the width:"))       
area(h,w)

'''
'''
num=[10,20,33,55,99]
for x in num:
    print(x)
print("max number is :",max(num))
    
'''
while True:
    inpt = input("Enter a number: ")
    if inpt == "done" : break

    try:
        num = int(inpt)
    except:
        print ("Invalid input")
    continue

largest = None
if largest is None:
    largest = num
elif num > largest:
    largest = num

smallest = None 
if smallest is None:
    smallest = num
elif num < smallest:
    smallest = num

print ("Maximum is", largest)
print ("Minimum is", smallest)
