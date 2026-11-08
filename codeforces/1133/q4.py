import sys


if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [n, k] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    a = [int(i) for i in sys.stdin.readline().rstrip().split()][::-1]
    
    d = {}
    
    s = n**2
    
    l = 0
    r = 2 #exclusive
    
    while r < n:
      checkset = {a[r]+1, a[r]+2, a[r]+3}
      
      d = 0
      for i in range(1,4):
        if a[r+i] in checkset:
          d += 1
          
      if d == 2:
        r+=1
        
      else:
        s += max(0, r-l-2)
        l = r+d-1
        r = l+2
        
        
        
    out.append(s%998244353)
        
          
      
        
        
    
      
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    