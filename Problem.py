f = open("Employers.txt", "a")
class Employer:
    def __init__(self, name, surename, age, staj, salary):
        self.name = name
        self.surename = surename
        self.age = age
        self.staj = staj
        self.salary = salary

    def info(self):
        print(f"Name {self.name}\nSurename {self.surename}\nAge {self.age}\nStaj {self.staj}\nSalary {self.salary}\n")

    def full_name(self):
        print(self.name, self.surename)

    def add_datas(self):
        lst = list()
        lst.append([self.name, self.surename, self.age, self.staj, self.salary])
        f.write(f"{', '.join(lst[0])}\n")   

E = Employer(input("Employer's name: "), input("Employer's surename: "), input("Employer's age: "), input("Employer's staj: "), input("Employer's salary: "))
E.add_datas()


class Developer(Employer):
    def __init__(self, name, surename, age, pro_language, staj, status, salary):
        self.pro_language = pro_language
        self.status = status
        super().__init__(name, surename, age, staj, salary)

    def add_datas(self):
        lst = list()
        lst.append([self.name, self.surename, self.age, self.pro_language, self.staj, self.status, self.salary])
        f.write(f"{', '.join(lst[0])}\n")

    def info(self):
        print(f"Name {self.name}\nSurename {self.surename}\nAge {self.age}\nProgramming language {self.pro_language}\nStaj {self.staj}\nStatus {self.status}\nSalary {self.salary}\n")

D = Developer(input("Developer's name: "), input("Developer's surename: "), input("Developer's age: "), input("Developer's programming language: "), input("Developer's staj: "), input("Developer's status: "), input("Developer's salary: "))
D.add_datas()
        

f.close()