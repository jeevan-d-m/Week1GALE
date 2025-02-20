phone_map ={}
class ContactDetail():
    def __init__(self,Contact_Number,Address, name):
        if phone_map.__contains__(Contact_Number):
            raise Exception ("phone number Exists")
        self.Contact_Number=Contact_Number
        self.Address = Address
        self.name = name
        phone_map[Contact_Number] = self

    # def __str__(self):
    #     print(f"name :{self.name} : contact number : {self.Contact_Number} Address : {self.Address}")

    def display(self):
        print(self.Contact_Number)
        print(self.Address)
    

    # def __str__(self):
    #     return f"{self.Contact_Number}"

class Person():
    def __init__(self,name,employee_id,email,designation,salary, contactdetail):
        self.name=name
        self.employee_id=employee_id
        self.email=email
        self.designation=designation
        self.salary=salary
        self.contcatdetail = contactdetail

    def display_contactDetail(self):
        print(self.name)
        print(self.id)
        print(self.email)
        print(self.designation)
        print(self.salary)
        print(self.contcatdetail)

class Employee(Person):
    def __init__(self, name, id, email, designation, salary, contactdetail, experience, DOB):
        super().__init__(name, id,email, designation, salary, contactdetail)
        self.experience = experience
        self.DOB = DOB
    
    def __str__(self):
        return f"{self.name} has a salary {self.salary}"


def get_name(number):
    contact = phone_map[number] 
    print(f"The name of emp with number {number} is {contact.name}")

    pass

def get_number(id,employees:list):
    for employee in employees:
        if employee.employee_id == id:
            print(f"{employee.name}'s phone number is {employee.contcatdetail.Contact_Number}")
    pass


contact1 = ContactDetail("9886468304","Mysore" ,"jeevan")
contact2 = ContactDetail("6886468304","Nanjangud", "yashwanth")
contact3 = ContactDetail("7338234250","Hassan","Nikhil")
# print(contact2.Address)

emp1 = Employee("jeevan",1,"abc@gmail.com","intern",15000,contact1,11,"28/01/2004")
emp2 = Employee("yashwanth",2,"def@gmail.com","fulltime",20000,contact2,12,"01/01/2006")
emp3 = Employee("nikhil",3,"hij@gmail.com","part-time",25000,contact3,8,"05/06/2007")





# for key ,value in phone_map.items():
#     print(f"{key} : {value.name} {value.Contact_Number} {value.Address} ")

get_name("9886468304")

get_number(2,[emp1, emp2,emp3])
