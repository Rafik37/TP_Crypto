import random
import sys
from math import sqrt
from common import *

####################
# Q14
####################

# retourne p g 
# g generateur sur le groupe Z*p => on utilise 3
# p premier sur n bits.
def gen_elgamal_pg(n):
    return 0
    
####################
# Q15
####################

# retourne couple cle prive/publique [sk,pk]
# definit tel que sk compris entre (3,p-2) 
# pk =  g^sk [p]
# output: [sk,pk]
def gen_elgamal_sk_pk(p,g):
    return 0

####################
# Q16
####################
    
# pk_a,sk_a,pk_b,sk_b sont les cles publiques prive de A B modulo p
# retourne le secret partage par A et B
def gen_elgamal_get_secret(pk_a,sk_a,pk_b,sk_b,p):
    return 0

####################
# Q17
####################

# chiffrement du message m avec le secret
# output: chaine de charactere c en binaire  represantant c 
# cotrainte: secret plus grand que message 
def enc_elgamal(m,secret,p):
    # indice transormez le message (et le secret en binaire) en binaire:
    # bin_m = bin(str_to_int(m))[2:]  
    return 0

# dechiffrement du message c avec le secret
# output: chaine de charactere m 
# cotrainte: secret plus grand que message
def dec_elgamal(c,secret,p):        
    return 0 


####################
# Q19
####################
 
# retourne la signatue [r, s]
# sk cle secrete utilise pour signer message m
# m sous forme de texte     
def elgamalsignature(g,p,sk,m):
	return 0
    
# r,s signature
# pk cle publique utilise pour signer message m
# m sous forme de texte 
# output: bool verifie si signature valide
# true = valid  
def elgamalverification(g,p,r,s,m,pk):
    return 0  
