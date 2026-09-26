import pickle
class Employeeview:
    def viewemployees(self):
        self.records=[]
        with open("F:\\Bhavana python\\project on oops\\Details.pick", "rb") as fp:
            print("-" * 50)
            print("\tENO\t\tNAME\tSAL\t\tDESIGNATION")
            print("-" * 50)
            while(True):
                try:
                    self.record = pickle.load(fp)
                    self.records.append(self.record)
                    print(f"\t{self.record[0]}\t\t{self.record[1]}\t{self.record[2]}\t\t{self.record[3]}")
                except EOFError:
                    break
        #print(self.records)
    def viewemployee(self):
        eno = int(input("Enter employee number to view the details:"))
        res = False
        for record in self.records:
            if (record[0] == eno):
                emprec = record
                res = True
                break
        print("-" * 50)
        if (res):
            print("\tEmployee Number:{}".format(emprec[0]))
            print("\tEmployee Name:{}".format(emprec[1]))
            print("\tEmployee Salary:{}".format(emprec[2]))
            print("\tEmployee Designation:{}".format(emprec[3]))
        else:
            print("\tEmployee Details Does Not Exist--invalid employee ")

#o=Employeeview()
#o.viewemployees()
#o.viewemployee()
