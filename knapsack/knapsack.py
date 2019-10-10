#!/usr/bin/python

import sys
from collections import namedtuple


#from https://www.w3resource.com/python-exercises/data-structures-and-algorithms/python-search-and-sorting-exercise-4.php
#i would normally create a class called items and creat a __gr__() to represent the a>b but because this started as a named tuple i cant do this
def bubbleSort(nlist):
    for passnum in range(len(nlist)-1,0,-1):
        for i in range(passnum):
            if nlist[i].value/nlist[i].size<nlist[i+1].value/nlist[i+1].size: #changed the condition a lil here
                temp = nlist[i]
                nlist[i] = nlist[i+1]
                nlist[i+1] = temp
    return nlist;


Item = namedtuple('Item', ['index', 'size', 'value'])
def knapsack_solver(items, capacity):
  bubbleSort(items); #sort this so that the most value per unit size. ie value/size; this will give us the most "valuable units in the front of the list;
  arr = []
  totalsize = 0;
  totalvalue = 0;
  for i in items: #now we just select each item that fits since we know that the most valueable items are gonna be put in first
    if(i.size + totalsize <= capacity):
      totalsize += i.size;
      totalvalue += i.value;
      arr.append(i.index);
  return f"Items to select: {arr}\nTotal cost:{totalsize}\nTotal value:{totalvalue}";

if __name__ == '__main__':
  if len(sys.argv) > 1:
    capacity = int(sys.argv[2])
    file_location = sys.argv[1].strip()
##  else:
##    file_location = "data/large1.txt";
##    capacity = 1000;
    file_contents = open(file_location, 'r')
    items = []

    for line in file_contents.readlines():
      data = line.rstrip().split()
      items.append(Item(int(data[0]), int(data[1]), int(data[2])))
    
    file_contents.close()
    print(knapsack_solver(items, capacity))
  else:
    print('Usage: knapsack.py [filename] [capacity]')

