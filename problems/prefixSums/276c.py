import sys





if __name__ == "__main__":
  [n,q] = [int(i) for i in sys.stdin.readline().strip().split()]
  vals = sorted([int(i) for i in sys.stdin.readline().strip().split()], reverse = True)
  
  v = [0]*(n+1)
  
  for _ in range(q):
    [l,r] = [int(i) for i in sys.stdin.readline().strip().split()]
    v[l-1] += 1
    v[r] -=1
    
  d = {}
  
  for i in range(q+1):
    d[i] = 0
    
  c = 0
  
  for i in v[:-1]:
    c += i
    d[c] += 1
    
  s = 0
  c = 0  
  for i in range(q, -1, -1):
    for _ in range(d[i]):
      s += i*vals[c]
      c += 1
  
  
  sys.stdout.write(str(s) + '\n')
  
    
  
  
  
  
    