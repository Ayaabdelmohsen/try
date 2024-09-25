class employees:
    "this is a employee class"
    empCount = 0

    def __init__(self,name,age,salary=3000,nId=295455,position='engineer'):
        self.Name = name
        self.Age = age
        self.Salary = salary
        self.NId = nId
        self.Posision = position
        employees.empCount += 1

    def __del__(self):
        employees.empCount -= 1
        
    def displayEmployee(self):
        return self.Name +" " + str(self.Age)+" " +str(self.Salary)
    
    def displayCountOfEmployees():
        return "the no of employees in our company is: "+str(employees.empCount)

print(employees.empCount)
emp1 = employees('abdo shokry',18,20000,3565222555,'django developer')
emp2 = employees('ahmed osama',18,20000,3565222555,'python developer')
emp3 = employees('saher',18,20000,3565222555,'graphic designer')
emp4 = employees("islam",34)
# print(emp1.Name)
# print(getattr(emp1,'Name'))
# print(setattr(emp1,'Name','abdo mostafa shokry'))
# print(getattr(emp1,'Name'))
# emp1.Name = "islam"
# print(getattr(emp1,'Name'))
print(employees.empCount)
# print(emp1.empCount)
# print(emp4.Salary)
# print(emp1.displayEmployee())
# print(employees.displayCountOfEmployees())

# print(employees.__name__)
# print(employees.__dict__)

del emp3
print(employees.empCount)
