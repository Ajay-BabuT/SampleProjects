class A:
    def disp(self):
        print("A")
class B(A):
    def disp(self):
        print("B")
        super().disp()
ob=B()
ob.disp()
