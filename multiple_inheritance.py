class A(object):
    def dothis(self):
        print('doing this in A')

class B(A):
    pass



class C(object):
    def dothis(self):
        print('doing this in C')



class D(B,A):
    pass



d=D()
d.dothis()
print(D.mro())


