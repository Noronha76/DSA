
#map
#map(func, *iterables)
def fahrenheit(T):
    return ((9.0/5)*T + 32) 
temp = [0,22.5,25,80]
print('map : ',list(map(fahrenheit,temp)))


# reduce
#reduce(function, iterable[, initializer])
from functools import reduce
lista1 = [1,5,78,23,75,22]
print('reduce : ',reduce(lambda x,y: x+y, lista1))

#filter
#filter(functionorNone, iterable)
def primo(n):
    count = n
    eprimo = True
    while count > 2:
        count -= 1
        if n%count == 0:
            eprimo = False
    return eprimo
lista50 = list(range(3,51))
print('filter : ', list(filter(primo,lista50)))

# list comprehension
def eprimo(n):
    count = n
    eprimo = True
    while count > 2:
        count -= 1
        if n%count == 0:
            eprimo = False
    return eprimo
print('list comprehension : ', [x for x in range(3,51) if eprimo(x)])
# list comprehension (aninhada)
print('list comprehension (aninhada) : ', [ x**2 for x in [x**2 for x in range(11)]])