import re
gd="Manu got 80 marks,mahesh got 67 marks,rashi got 919 marks,shobha got 98 marks"
print("------------------------------------")
print("marks of students")
markslist=re.findall("\d{2,3}",gd)
for marks in markslist:
    print(marks)
#kkk
import re
gd="manu got 9 marks,sedsilly got 1 marks,lavi got 100 marks,Honey got 99 marks"
print("=======================")
print("marks of students")
markslst=re.findall("\d{1,3}",gd)
for marks in markslst:
    print(marks)
#33
import re
gd="sedsilly got 200 marks,i got 100 marks,honee got 0 marks"
print("==================================================================================================")

print("marks of sedsilly:")
markslists=re.findall("\d{1,3}",gd)
for marks in markslists:
    print(marks)
#kkkk
import re
gd="i got 2,i got 3,honey got 4,binitha got 4,sed silly got 5"
print("===========================================================")
print("sedsilly's gf marks: binitha:::")
markslistts=re.findall("\d{1,3}",gd)
for marks in markslistts:
    print(marks)
#loop
s=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
for i in s:
    print(i)
#999
import re
sd="lavi got 100,silly got 200,bhura ki binitha got 300"
print("-----------------------------------------------------")
print("sedsilly's gf :      binitha:::::::binitha::::binitha------>>>>>>>>>>>binitha::")
marklsst=re.findall("\d{1,3}",sd)
for marks in marklsst:
    print(marks)
#pickl
import pickle
cars=["lvy","lamborgini urus","maruthi suzuki"]
file="mycar.pkl"
fileobj=open(file,'wb')
pickle.dump(cars,fileobj)
fileobj.close()
#
file="mycar.pkl"
fileobj=open(file,'rb')
mycar=pickle.load(fileobj)
#n
n=int(input("enter:"))
if(n<=0):
    print("{} is invalid".format(n))
else:
    print("\tnat nums\tsquares\tcubes")
    i=1
    s,ss,cs=0,0,0
    while(i<=n):
        print("\t{}\t\t{}\t{}".format(i,i**2,i**3))
        i=i+1
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
    else:
        print("="*50)
        print("\t{}\t\t{}\t{}".format(s,ss,cs))
#ll4
n =int(input("ent:"))
if(n<=0):
    print("{} is invLID".format(n))
else:
    print("\tnatnum\tsquares\tcubes")
    s,ss,cs=0,0,0
    for i in range(n,n+1):
        print("\t{}\t\t{}\t{}".format(i,i**2,i**3))
        s=s+i
        ss=ss+i**2
        cs=cs+i**3
        i=i+1
    else:
        print("="*50)
        print("\t{}\t\t{}\t{}".format(s,ss,cs))

#5++
n=int(input("ent:"))
if(n<=0):
    print("{} is invalid".format(n))
else:
    for i in range(1,n+1):
        if(n%1==0):
            print("\t{}".format(i))