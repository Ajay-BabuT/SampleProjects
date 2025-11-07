class Number:
    def get(self):
        self.n=10
    def put(self):
        print("n=",self.n)
    def __mul__(self,other):
        t=Number()
        t.n=self.n*other.n
        return t
ob1=Number()
ob2=Number()
ob3=Number()
ob1.get()
ob2.get()
ob3=ob1*ob2 #calls add() method
ob1.put()
ob2.put()
ob3.put()
