#EmployeeUpdate.py
import pickle
class Employeeupdate:
    def __init__(self):
        self.records = []
        with open("F:\\Bhavana python\\project on oops\\Details.pick", "rb") as fp:
            while True:
                try:
                    self.record = pickle.load(fp)
                    self.records.append(self.record)
                except EOFError:
                    break
        #print(self.records)
    def updateemployee(self):
        while(True):
            eno = int(input("Enter employee number to update:"))
            res = False
            for record in self.records:
                if (record[0] == eno):
                    emprec = record
                    res = True
                    break
            if (res):
                newsal = float(input("Enter new employee salary:"))
                emprec[2] = newsal
                newdsg = input("Enter new employee designation:")
                emprec[3] = newdsg
                with open("F:\\Bhavana python\\project on oops\\Details.pick", "wb") as fp:
                    for record in self.records:
                        pickle.dump(record, fp)
                print("Employee Record Updated")
                ch=input("Do you want to update employee details?(yes/no):")
                if(ch.lower()=="no"):
                    break
            else:
                print("Employee Record Not Found")
                break
#o=Employeeupdate()
#o.updateemployee()



