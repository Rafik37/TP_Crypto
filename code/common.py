import random
import sys
from math import sqrt


####################
# Q1
####################

# retourne le pgcd de deux entiers naturels
def pgcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

# algo euclide etendu
# retourne d,u,v avec pgcd(a,b)=d=ua+vb
def euclide_ext(a,b):
    if b == 0:
        return a, 1, 0

    d, u, v = euclide_ext(b, a % b)
    u, v = v, u - (a // b) * v

    return d, u, v
    
####################
# Q2
####################

# retourne un entier b dans [1,N-1] avec ab=1 modulo N
def inverse_modulaire(N,a):
    d, u, v = euclide_ext(a, N)
    if d != 1:
        return None
    else:
        return u % N

####################
# Q3
####################

# retourne (b**e) % n
# calcule le modulo apres chaque multiplication
def expo_modulaire(e,b,n):
    res = 1
    base = b % n

    for i in range(e):
        res = (res * base) % n

    return res

####################
# Q4
####################

# retourne (b**e) % n
# calcule le modulo apres chaque multiplication
# O(log(e)) operations
def expo_modulaire_fast(e,b,n):
    # help:
    
    # representer e en binaire
    #bin_e = bin(e)[2:]
    
    # utile pour iterer sur chaque element de e 
    #for x in range(len(bin_e)):
    #   int(bin_e[x])
    
    bin_e = bin(e)[::-1]
    res = 1
    base = b % n

    for digit in bin_e:
        if digit == '1':
            res = (res * base) % n
        base = (base * base) % n

    return res

####################
# Q5
####################

# retourne la liste des nombres premiers <= n
# methode du crible d Eratosthene
def crible_eras(n):
    #initialisation de la liste des nombres premiers
    primes = [True]*(n+1)
    primes[0] = primes[1] = False
    #application du crible
    for i in range(2, int(n**0.5)+1):
        if primes[i]:
            for j in range(i*i, n+1, i):
                primes[j] = False
    #construction de la liste finale des nombres premiers
    primes_list = []
    for k in range(2, n+1):
        if primes[k]:
            primes_list.append(k)
    return primes_list
        
####################
# Q6
####################

# input: n  
# input: t number of tests
# test if prime according to fermat
# output: bool if prime 
def test_fermat(n,t):
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    for i in range(t):
        a = random.randint(2, n-2)
        if expo_modulaire_fast(n-1,a,n) != 1:
            return False
    return True

####################
# Q7
####################

# input: n
# output: r and u coefficient
# for rabin test 
# returns r,u such that 2^r * u = n and u is odd
def find_ru(n):
    r = 0
    u = n

    while u % 2 == 0:
        r += 1
        u //= 2

    return r, u  

####################
# Q8
####################

#n entier
#a entier dans [1,n-2]
#pgcd(a,n)=1
#retourne True , si a est un temoin de Rabin de non-primalite de n
def temoin_rabin(a,n):
    # utilisez expo_modulaire_fast !
    r, u = find_ru(n)
    x = expo_modulaire_fast(a, u, n)
    if x == 1 or x == n - 1:
        return False
    for _ in range(1, r):
        x = (x * x) % n
        if x == n - 1:
            return False
    return True


#n entier a tester, t nombre de tests
#retourne True , si n est premier
#retourne False , avec proba > 1-(1/4)**t, si n est compose
def test_rabin(n,t):
    if n == 2:
        return True
    if n < 2 or n % 2 == 0:
        return False
    
    for _ in range(t):
        a = random.randint(2, n - 1)
        if temoin_rabin(a, n):
            return False
    
    return True  
            
# prime generator
# output: n range for prime number
# utilise votre implementation de rabin (ou la plus effice si rabin non dispo)
# pour generer un nombre premier sur n bits.
# range de n: p = random.randint(pow(2,n-1),pow(2,n)-1)
def gen_prime(n):
    p = random.randint(pow(2,n-1),pow(2,n)-1)
    while not test_rabin(p, 10):
        p = random.randint(pow(2,n-1),pow(2,n)-1)
    return p

####################
# Helper functions for rsa/elgamal
####################

# Helper function
# convert str to int
def str_to_int(m):
    s = 0
    b = 1
    for i in range(len(m)):
        s = s + ord(m[i])*b
        b = b * 256
    return s

# Helper function
# convert int to str
def int_to_str(c):
    s = ""
    q,r = divmod(c,256)
    s = s+str(chr(r))
    while q != 0:
        q,r = divmod(q,256)
        s = s+str(chr(r))
    return s
