#!/usr/bin/python

import sys

def making_change(amount, denominations=[1,5,25,50]):
  count = 1;
  if(len(denominations) < 2 or amount < denominations[1]): #just a wierd corner case
    return 1;
  if amount > denominations[1]: #if all we have left is pennies we only have the base 1 way;
    for d in denominations:
      if(d < 2):
        continue;
      a = amount // d;
      count += a;
      if(a > 0 and amount > 4):
        count += making_change(amount-a*d, denominations);
      
  return count;


if __name__ == "__main__":
  for i in range(0,51):
    print(making_change(i))
  # Test our your implementation from the command line
  # with `python making_change.py [amount]` with different amounts
  if len(sys.argv) > 1:
    denominations = [1, 5, 10, 25, 50]
    amount = int(sys.argv[1])
    print("There are {ways} ways to make {amount} cents.".format(ways=making_change(amount, denominations), amount=amount))
  else:
    print("Usage: making_change.py [amount]")
