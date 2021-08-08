'''
class calc:
    def __init__(self,a,b):
        self.a=a
        self.b=b
   


    def add(self):
        return self.a+self.b

        
    def sub(self):
        return self.a-self.b


    def mull(self):
        return self.a*self.b


    def div(self):
        return self.a/self.b


class scicalc(calc):
    def power(self):
        #return pow(self.a,self.b)
        return self.a ** self.b




c=scicalc(4,2)
print(c.add())
print(c.sub())
print(c.mull())
print(c.div())
print(c.power())
'''
#________________________________________________________#
'''
class animal(object):
    def __init__(self,name,food):
        self.name=name
        self.food=food
        print("{} is eating {}".format(name,food))


class dog(animal):
    def fetch(self ,thing):
        print("{}is eating {}".format(self.name,thing))



class cat(animal):
    def eat(self):
        print("{} is eating food".format(self.name))


a=animal("lion","meat")
d=dog("dog","chicken")
c=cat("cat",'fish')
print(d.fetch("chick"))
print(c.eat())
'''
#________________________________________________________#
'''
class Date():
    def get_date(self):
        return("24-4-2020")


class Time(Date):
    def get_time(self):
        return ("3:47:50")



d=Date()
print(d.get_date())
t=Time()
print(t.get_time())
print(t.get_date())


'''
#___________________________________________________________#






































