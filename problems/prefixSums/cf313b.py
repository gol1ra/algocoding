import sys


def main():
  
  s = sys.stdin.readline().strip()
  m = int(sys.stdin.readline())
  
  
  psum = [0]*len(s)
  
  for i in range(1,len(s)):
    psum[i] = psum[i-1]
    if s[i] == s[i-1]:
      psum[i] += 1
  
  # print(psum)
    
    
  
  out = []
  
  for _ in range(m):
    [l,r] = [int(i) for i in sys.stdin.readline().strip().split()]
    l-=1
    r-=1
    
    k=0
    if l>0:
      k = psum[l]
    out.append(psum[r]-k)
  
  
  sys.stdout.write("\n".join(map(str, out)) + '\n')
    
    
if __name__ == "__main__":
  main()