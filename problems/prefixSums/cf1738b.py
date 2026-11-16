import sys


if __name__ == "__main__":
  t = sys.stdin.readline()
  out = []
  def check(n, k, vals):
    if k == 1:
      out.append("Yes")
      return
    
    bar = vals[1] - vals[0] if n != k else vals[0]
    
    if (n-k+1) * bar < vals[0] and n!=k:
      out.append("No")
      return
    
    for i in range(0, k-1):
      d = vals[i+1] - vals[i]
      if d < bar:
        out.append("No")
        return
      else:
        bar = d
        
        
    out.append("Yes")
    return 
        
    
        
  for _ in range(int(t)):
    [n,k] = [int(i) for i in sys.stdin.readline().strip().split()]
    vals = [int(i) for i in sys.stdin.readline().strip().split()]
    
    check(n,k,vals)
        
  sys.stdout.write("\n".join(out) + "\n")