import sys
from math import floor


def main(h,n,a,c):
  
  def valid(moves):
    return sum([a[i] * ((moves + c[i] - 1)//c[i]) for i in range(len(c))]) >= h 
  
  lo = 0
  hi = h * max(c) + 1    
  mid = (lo + hi)//2
  
  while lo < hi: 
  
    if valid(mid):
      hi = mid   
    else:
      lo = mid + 1   
    mid = (lo + hi)//2

  return mid

if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [h,n] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    a = [int(i) for i in sys.stdin.readline().rstrip().split()]
    c = [int(i) for i in sys.stdin.readline().rstrip().split()]

    out.append(main(h,n,a,c))
  
  
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    