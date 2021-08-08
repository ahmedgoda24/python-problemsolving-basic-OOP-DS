'''
class student:
    def __init__(self,name):
        self.name=name
        self.marks=[]
        print('welcome {} in the school'.format(name))

    def add_marks(self , mark):
        self.marks.append(mark)


    def avg(self):
        return sum(self.marks)/len(self.marks)




s1 = student('ahmed')
print(s1.marks)
s1.add_marks(90)
s1.add_marks(80)
s1.add_marks(70)
s1.add_marks(60)
s1.add_marks(50)
print(s1.marks)


print(s1.avg())
'''


class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
   


    def add(self):
        return self.a+self.b
        print('this is addition')

        
    def sub(self):
        return self.a-self.b
    print('this is subtion')


    def mull(self):
        return self.a*self.b
    print('this is multibation')

    def div(self):
        return self.a/self.b
    print('this is division')






c=calc(10,20)
print(c.add())
print(c.sub())
print(c.mull())
print(c.div())

