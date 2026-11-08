import sys


def main():
  
  n = int(sys.stdin.readline())

  v = [int(i) for i in sys.stdin.readline().strip().split()]
  
  psum = list(v)
  for i in range(1,n):
    psum[i] += psum[i-1]
    
  spsum = list(sorted(v))
  for i in range(1,n):
    spsum[i] += spsum[i-1]
  
  
  m = int(sys.stdin.readline())
  
  out = []
  
  for _ in range(m):
    [t,l,r] = [int(i) for i in sys.stdin.readline().strip().split()]
    r-=1
    l-=1
    
    k = 0
    if t == 1:
      if l >0:
        k = psum[l-1]
      out.append(psum[r]-k)
    else:
      if l >0:
        k = spsum[l-1]
      out.append(spsum[r]-k)
  
  
  sys.stdout.write("\n".join(map(str, out)) + '\n')
    
    
if __name__ == "__main__":
  main()