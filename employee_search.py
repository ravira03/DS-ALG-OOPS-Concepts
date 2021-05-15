class Employee:
    def __init__(self, name, emp_id, email_id):
        self.__name=name
        self.__emp_id=emp_id
        self.__email_id=email_id

    def get_name(self):
        return self.__name

    def get_email_id(self):
        return self.__email_id
    
    def get_emp_id(self):
        return self.__emp_id

class OrganizationDirectory:
    def __init__(self,emp_list):
        self.__emp_list=emp_list

    def lookup(self,key_name):
        result = []
        for emp in self.__emp_list:
            if(key_name in emp.get_name()):
                result.append(emp)
        self.display(result)
        return result

    def display(self,result):
        print("Search Result's are")
        for emp in result:
            print(emp.get_name()," ",emp.get_emp_id()," ",emp.get_email_id())
        

emp1 = Employee("ravi",24809,"ravivarmara22@gmail.com")
emp2 = Employee("ravivarma",25809,"ravivarma22@gmail.com")
emp3 = Employee("arun",26809,"arun07@gmail.com")
emp4 = Employee("bala",27809,"balasunder@gmail.com")

emp_list=[emp1,emp2,emp3,emp4]


org_dir = OrganizationDirectory(emp_list)

org_dir.lookup("ravi")