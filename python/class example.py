class student:
    def read(self):
        self.rollno=int(input("Enter rollno : "))
        self.name=input("Enter name : ")
    def show(self):
        print("Rollno is ",self.rollno)
        print("Name is ",self.name)
s1=student()
s1.read()
s1.show()
