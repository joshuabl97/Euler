#!/usr/bin/python3

#The prime factors of 13195 are 5, 7, 13 and 29.

#What is the largest prime factor of the number 600851475143 ?

import math 

x = 600851475143 
factor = 3  

while (x > 1): 
    if(x % factor == 0):
        x/=factor 
    else: 
        factor +=2

print(factor) 
