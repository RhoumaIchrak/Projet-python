file = open("connexion.log.txt","r")
file2 = open("utilisateurs.txt","a")
lines = file.readlines()
for i in lines:
   # print(i.split(";")[1])
    file2.write(i.split(";")[1]+"\n")

file.close()
file2.close()


#Question2

file = open("connexion.log.txt","r")

r=[]
for i in lines :
   r.append(i.split(";")[2]) 
for i in r :
    print(i.split()[1])
#print(r)
tm=[]
for i in lines :
    tm.append(i.split()[1])
for i in tm :
    print(i.split(":")[0])






  