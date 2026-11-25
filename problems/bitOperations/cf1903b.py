import sys

from functools import reduce
from operator import and_


def main(v):
  r = []
  for key, i in enumerate(v):
    r.append(reduce(and_, [j for k, j in enumerate(i) if k != key],-1))  
  
  for i in range(n):
    for j in range(n):
      if r[i] | r[j] != v[i][j] and i!=j:
        return []
      
  return r

if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    n = int(sys.stdin.readline().rstrip())
    v = [[int(i) for i in sys.stdin.readline().rstrip().split()] for _ in range(n)]
    
    if n > 1:
      r = main(v)
    else:
      r = [1]
    
    if len(r) != 0:
      out.append('yes')
      out.append(" ".join(map(str, r)))
      
    else:
      out.append('no')
  
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    