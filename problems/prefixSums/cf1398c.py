import sys

if __name__ == "__main__":
  t = sys.stdin.readline()
  
  for _ in range(int(t)):
    n = int(sys.stdin.readline())
    k = int(sys.stdin.readline())
    v = []
    
    for _ in range(n):
      v.append(k%10)
      k = k%10
      
    for i in range(1,n):
      v[i]+=v[i-1]
      
      
    def subsum(l,r):
      minus = 0
      if l > 0:
        minus = v[l-1]
      return v[r] - minus
    
    print("! YES", flush=True)