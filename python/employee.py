class Employee:
    def read(self):
        self.id=int(input("Enter id : "))
        self.name=input("Enter name : ")
        self.salary=int(input("Enter salary : "))
    def show(self):
        print("ID is ",self.id)
        print("Name is ",self.name)
        print("Salary is ",self.salary)
e1=Employee()
e1.read()
e1.show()
