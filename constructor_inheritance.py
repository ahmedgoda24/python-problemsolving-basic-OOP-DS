class animal(object):
    def __init__(self,name,age):
        self.name=name
        self.age=age


class dog(animal):
    def __init__ (self,name,age):
        super(dog,self).__init__(name,age)
        self.food="meat"





a=animal("rox",2)
print(a.name,"\n",a.age)
d=dog("rooo",3)
print(d.name,"\n",d.age,"\n",d.food)
