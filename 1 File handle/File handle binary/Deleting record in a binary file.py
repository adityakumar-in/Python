import pickle
def Bdelete():
    F= open("studrec.dat","rb")
    stud = pickle.load(F)
    F.close()
    print(stud)
    rno= int(input("Enter the roll number to be deleted"))
    F= open("studrec.dat","wb")
    rec= []
    for i in stud:
        if i[0] == rno:
            continue
        rec.append(i)
    pickle.dump(rec,F)
    F.close()
Bdelete()
