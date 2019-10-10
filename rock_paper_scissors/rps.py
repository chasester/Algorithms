#!/usr/bin/python

import sys


def rock_paper_scissors(n, i=0):
  

if __name__ == "__main__":
  rock_paper_scissors(2);
  if len(sys.argv) > 1:
    num_plays = int(sys.argv[1])
    print(rock_paper_scissors(num_plays))
  else:
    print('Usage: rps.py [num_plays]')
