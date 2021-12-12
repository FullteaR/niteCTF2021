import numpy as np
from scipy import linalg
import sympy as sp

Ciphertext = [8194393930139798, 7130326565974613, 9604891888210928, 6348662706560873, 11444688343062563, 7335285885849258, 3791814454530873, 926264016764633, 9604891888210928, 5286663580435343, 5801472714696338, 875157765441840, 926264016764633, 2406927753242613, 5980222734708251, 5286663580435343, 2822500611304865, 5626320567751485, 3660106045179536, 2309834531980460, 12010406743573553]


sp.var("a,b,c,d")

eqs = []
for i,x in zip(Ciphertext,"nite"):
    eqs.append(sp.Eq(a*pow(ord(x),3)+b*pow(ord(x),2)+c*ord(x)+d, i))


s = sp.solve(eqs, [a,b,c,d])
sp.init_printing()
a, b, c, d = s[a], s[b], s[c], s[d]
print(a,b,c,d)

for i, x in enumerate("nite"):
    assert (a*pow(ord(x),3)+b*pow(ord(x),2)+c*ord(x)+d)==Ciphertext[i]

for i in Ciphertext:
    for x in range(256):
        if i == a*pow(x,3)+b*pow(x,2)+c*x+d:
            print(chr(x), end="")
print()
