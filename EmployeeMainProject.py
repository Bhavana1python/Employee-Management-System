#EmployeeMainProject.py
from EmpMenu import menu
from EmployeeAdd import details
from EmployeeDelete import employeedelete
from EmployeeUpdate import Employeeupdate
from EmployeeView import Employeeview
from EmployeeSearch import EmployeeSearch
a=details()
d = employeedelete()
u=Employeeupdate()
v=Employeeview()
s=EmployeeSearch()
while(True):
    menu()
    ch=int(input("Enter ur choice:"))
    match (ch):
        case 1:
            a.saveempdata()
        case 2:
            d.deleteemployee()
        case 3:
            u.updateemployee()
        case 4:
            v.viewemployee()
        case 5:
            v.viewemployees()
        case 6:
            s.searchemp()
        case _:
            print("Invalid choice----Try again")





