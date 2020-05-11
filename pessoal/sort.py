import random
lsta, lstb = [], []
[lsta.append(random.randint(1,10)) for i in range(10)]
[lstb.append(random.randint(1,10)) for i in range(10)]
print('listas originais : ',lsta,lstb)
lst2 = lsta.sort()
print('lista A ordenada : ',lsta) #doidera
for i in range(10):
    for ii in range(i+1,10):
        if(lstb[i] > lstb[ii]):
            lstb[i], lstb[ii] = lstb[ii], lstb[i]
print('lista B ordenada : ',lstb)
