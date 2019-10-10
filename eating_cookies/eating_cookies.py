#!/usr/bin/python

import sys
import math;
# The cache parameter is here for if you want to implement
# a solution that is more efficient than the naive 
# recursive solution
cache = [0 for i in range(0, 2**27) ] #the normal size of int on a x86 archeture;

def eating_cookies(n): #why would you did it as a paramater?
  if(n < 0 ):
    return flaot('Nan');
  
  a = [1,1,2,4]; #these are the answers at each index so f(0)=1 f(1) =1 f(2)=2 etc
  if(n < len(a)):
    return a[n];
  
  cache[n] = cache[n] if cache[n] > 0 else eating_cookies(n-1) + eating_cookies(n-2) + eating_cookies(n-3);
  return cache[n];

if __name__ == "__main__":
##  for i in range(0, 30000):
##    print(eating_cookies(i));
  if len(sys.argv) > 1:
    num_cookies = int(sys.argv[1])
    print("There are {ways} ways for Cookie Monster to eat {n} cookies.".format(ways=eating_cookies(num_cookies), n=num_cookies))
  else:
    print('Usage: eating_cookies.py [num_cookies]')
