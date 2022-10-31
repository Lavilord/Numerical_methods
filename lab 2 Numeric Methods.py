import numpy as np

#Метод поділу ділянки навпіл з пошуком ділянки локалізації
#x[0,1; 4]
#sin(x / 4) - ln(x) = 0

e = 0.0000000000001
h = 3.9
a = 0.1
b = a + h

fa = np.sin(a) - np.log(a)
fb = np.sin(b) - np.log(b)

if (np.abs(fb) > np.abs(fa)) and (fa * fb > 0):
    h = -1*h
    b = a + h
    fb = np.sin(b) - np.log(b)

while fa * fb > 0:
    a = b
    b = a + h
    fa = np.sin(a) - np.log(a)
    fb = np.sin(b) - np.log(b)

x = (b + a) / 2
fx = np.sin(x) - np.log(x)

while np.abs(fx) > e:
    x = (b + a) / 2
    fx = np.sin(x) - np.log(x)
    fa = np.sin(a) - np.log(a)
    if fa * fx > 0:
        a = x
    else:
        b = x

print (x)




