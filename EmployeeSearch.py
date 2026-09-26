#EmployeeSearch.py
import pickle
class EmployeeSearch:
    def __init__(self):
        self.records = []
        try:
            with open("F:\\Bhavana python\\project on oops\\Details.pick","rb") as fp:
                while(True):
                    try:
                        self.x = pickle.load(fp)
                        self.records.append(self.x)
                    except EOFError:
                        break
            for record in self.records:
                print(record)
            print()
        except FileNotFoundError:
            print("File does not exist")
    def searchemp(self):
        eno=int(input("Enter Employee Number:"))
        res=False
        for record in self.records:
            if(record[0]==eno):
                self.emprec=record
                res=True
                break
        if(res):
            print("Valid Employeee")
        else:
            print("Employee not found in the organization")

#o=EmployeeSearch()
#o.searchemp()