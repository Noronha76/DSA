import random
lst = []
[lst.append(random.randint(1,10)) for i in range(10)]
print('lista original : ',lst)
for i in range(10):
    for ii in range(i+1,10):
        if(lst[i] > lst[ii]):
            lst[i], lst[ii] = lst[ii], lst[i]
print('lista ordenada : ',lst)