#EmployeeDelete.py<---Module Name
import pickle
class employeedelete:
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
    def deleteemployee(self):
        while(True):
            eno = int(input("\tEnter employee number to delete the record:"))
            res = False
            for ind in range(len(self.records)):
                if (self.records[ind][0] == eno):
                    # del self.records[ind]   # ✅ only change
                    self.records.remove(self.records[ind])
                    print("\t\temployee deleted")
                    res = True
                    break
            if (res):
                with open("F:\\Bhavana python\\project on oops\\Details.pick", "wb") as fp:
                    for record in self.records:
                        pickle.dump(record, fp)
                    ch = input("Do u want delete another record(yes/no):")
                    if (ch.lower() == "no"):
                        break
            else:
                print("\tEmployee Record Does not Exist")
                break
            print("-" * 50)

#e = employeedelete()
#e.deleteemployee()