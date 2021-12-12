from pwn import *
from Crypto.Util.number import *
from fermat import fermat
from sympy.ntheory.modular import crt



io = remote("rabin.challenge.cryptonite.team", 1337)

for i in range(28):#banner
    io.recvline()
io.sendline(b"G")
io.recvline()
encrypted = io.recvline().decode().strip()
print(encrypted)

m = 2**250
M = 2**270


def check(x):
    io.sendline(b"E")
    io.recvline()
    io.sendline(bytes.hex(long_to_bytes(x)))
    io.recvline()
    square = io.recvline()
    square = int(square, 16)
    return square 

assert check(m) == m**2
assert check(M) != M**2

while M-m>1:
    mid = (M+m)//2
    if check(mid)==mid**2:
        m = mid
    else:
        M = mid
    print(M-m)

assert check(m)==m**2
assert check(M)!=M**2


n = M**2 - check(M)
print(n)

p, q = fermat(n)
print("p =", p)
print("q =", q)
c = int(encrypted, 16)
print("c =", c)