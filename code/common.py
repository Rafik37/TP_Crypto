import random
import sys
from math import sqrt


####################
# Q1
####################

# retourne le pgcd de deux entiers naturels
def pgcd(a,b):
    return 0

# algo euclide etendu
# retourne d,u,v avec pgcd(a,b)=d=ua+vb
def euclide_ext(a,b):
    return 0
    
####################
# Q2
####################

# retourne un entier b dans [1,N-1] avec ab=1 modulo N
def inverse_modulaire(N,a):
    return 0

####################
# Q3
####################

# retourne (b**e) % n
# calcule le modulo apres chaque multiplication
def expo_modulaire(e,b,n):
    return 0

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
    
    return 0

####################
# Q5
####################

# retourne la liste des nombres premiers <= n
# methode du crible d Eratosthene
def crible_eras(n):
    return []
        
####################
# Q6
####################

# input: n  
# input: t number of tests
# test if prime according to fermat
# output: bool if prime 
def test_fermat(n,t):
    # random number generator between a and b
    #x = random.randint(a,b)
    return True

####################
# Q7
####################

# input: n
# output: r and u coefficient
# for rabin test 
# returns r,u such that 2^r * u = n and u is odd
def find_ru(n):
    return 0  

####################
# Q8
####################

#n entier
#a entier dans [1,n-2]
#pgcd(a,n)=1
#retourne True , si a est un temoin de Rabin de non-primalite de n
def temoin_rabin(a,n):
    # utilisez expo_modulaire_fast !
    return 0


#n entier a tester, t nombre de tests
#retourne True , si n est premier
#retourne False , avec proba > 1-(1/4)**t, si n est compose
def test_rabin(n,t):
    return 0  
            
# prime generator
# output: n range for prime number
# utilise votre implementation de rabin (ou la plus effice si rabin non dispo)
# pour generer un nombre premier sur n bits.
# range de n: p = random.randint(pow(2,n-1),pow(2,n)-1)
def gen_prime(n):
    return 0

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
