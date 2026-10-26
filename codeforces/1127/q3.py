import sys
from math import sqrt, floor

def f(k):
  total = 0
  s = 1
  while s <= k:
    v = k // s
    s2 = k // v
    total += v * (s + s2) * (s2 - s + 1) // 2
    s = s2 + 1
  return total

if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [n] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    
    k = int(floor(sqrt(n)))
    st = f(k)
    if st >= n:
      while st >= n:
        k -= 1
        st = f(k)
      k += 1
    else:
      while st < n:
        k += 1
        st = f(k)
    
    a = []
    total = n
    currbag = 1
    for s in range(k, 0, -1):
      cnt = min(k // s, total // s)
      for _ in range(cnt):
        a += [currbag] * s
        currbag += 1
        total -= s
      if total == 0:
        break
    
    out.append(str(k))
    out.append(" ".join(map(str, a)))
    
  sys.stdout.write("\n".join(out) + "\n")