class a:
    def __init__(self,num):
        self.num=num
    def __add__(self, other):
         return self.num+other.num

a1 = a(10)
a2 = a(10)
print(a1+a2)