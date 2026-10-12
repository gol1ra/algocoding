import sys





if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  
  for _ in range(int(t)):
    n = int(sys.stdin.readline().rstrip())
    vals = [int(i) for i in sys.stdin.readline().rstrip().split()]
      
    max_s = vals[0]
    min_s = vals[0]
    r = vals[0]
    for v in vals[1::]:
        
      r = max(r, v, v + max_s, v - min_s)
      
      new_max_s = max(v, max_s + v, 2*max_s + v)
      new_min_s = min(v, min_s + v, 2*min_s + v)
      max_s, min_s = new_max_s, new_min_s
    
    out.append(r)
    
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    