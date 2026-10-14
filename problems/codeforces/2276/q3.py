

import sys



def main(k, v):
  c = 0
  
  
  rems = {}
  s = 0
  rems[0] = [0]
  for i in range(len(v)):
    s = (s + v[i]) % k
    rems.setdefault(s, []).append(i + 1)

  
      
  ds = {}
  for i, val in rems.items():
    ds[i] = []
    for j in range(len(val) - 1):
      ds[i].append(val[j+1] - val[j])

  for i, val in ds.items():
    
    l = 0
    d = 0
    for r in range(len(val)):
      d += val[r]
      while d > k:
        d -= val[l]
        l += 1
      c += l
      
      
      
      
  return c





if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [n, k] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    vals = [int(i) for i in sys.stdin.readline().rstrip().split()]
    
    out.append(main(k,vals))
      
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    