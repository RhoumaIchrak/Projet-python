from collections import Counter

file = open("warning.txt","r")
lines = file.readlines()
lst1 = []
for i in lines:
   # print(i.split(";")[1])
    lst1.append(i[:-1])

file.close()

file2 = open("connexion.log.txt","r")
lines2 = file2.readlines()

res = []
for ligne in lines2:
    if ligne.split(";")[0] in lst1:
        res.append(ligne.split(";")[1])

file2.close()

resdic = {}

for el in res:
    if el not in resdic.keys():
        resdic[el] = 1
    else:
        resdic[el] += 1

file3 = open("suspects.txt","w")

for i in resdic:
    file3.write("{};{}\n".format(i,resdic[i]))

file3.close()