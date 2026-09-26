import pickle
class details:
    def isunique(self,eno):
        self.records=[]
        with open("F:\\Bhavana python\\project on oops\\Details.pick", "rb") as fp:
            while(True):
                try:
                    self.record=pickle.load(fp)
                    self.records.append(self.record)
                except EOFError:
                    break
        res=True
        for record in self.records:
            if (record[0]==eno):
                res=False
        return res
    def saveempdata(self):
        while(True):
            with open("F:\\Bhavana python\\project on oops\\Details.pick","ab") as fp:
                print("-------------------------------------")
                #accept the employee values from KBD
                eno=int(input("Enter Employee Number: "))
                if (self.isunique(eno)):
                    self.ename = input("\tEnter Employee Name: ")
                    self.sal = float(input("\tEnter Employee Salary: "))
                    self.dsg = input("\tEnter Employee Designation: ")
                    print("-------------------------------------")
                    self.record = [eno,self.ename,self.sal,self.dsg]
                    # save the List object to the file
                    pickle.dump(self.record,fp)
                    print("Employee Record Saved in a File:")
                    ch = input("Do u want add another record(yes/no):")
                    if (ch.lower() == "no"):
                        break
                else:
                    print("\tEmployee Number already Exist--try with New Number")
                    break
                print("-------------------------------------")
#o=details()
#o.saveempdata()

