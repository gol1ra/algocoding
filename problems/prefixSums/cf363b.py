import sys


if __name__ == "__main__":
  [n,k] = [int(i) for i in sys.stdin.readline().strip().split()]
  vals = [int(i) for i in sys.stdin.readline().strip().split()]

  for i in range(1, len(vals)):
    vals[i] += vals[i-1]
    
  l = 1
  r = k-1
  m = vals[r]
  r+=1
  mi=0
  while r<n:
    if vals[r]-vals[l-1]<m:
      m = vals[r]-vals[l-1]
      mi = l
    l+=1
    r+=1
    
  sys.stdout.write(f'{mi+1}\n')