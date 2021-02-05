class Employee:
    no_of_employees=0
    salarylist = []
    def __init__(self, name,family,salary,department):
        self.name = name
        self.family = family
        self.salary = salary
        self.salarylist.append(salary)
        self.department = department
        Employee.no_of_employees +=1

    def average(self):
        sum_num = 0
        for t in self.salarylist:
            sum_num = sum_num + t

        avg = sum_num / len(self.salarylist)
        return avg


class FullTimeEmployee(Employee):
    pass

p1 = FullTimeEmployee("Paul","Walker",256,"software developer")
p2 = FullTimeEmployee("pachai","sundar",820,"software developer")
p3 = FullTimeEmployee("john","Myer",169,"software developer")
print("Average value : "+str(p1.average()))

print("no Of Employees : "+str(p1.no_of_employees))
print(p1.name)
print(p1.salarylist)