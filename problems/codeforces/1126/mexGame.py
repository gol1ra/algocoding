import sys

if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [n, k] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    c = [int(i) for i in sys.stdin.readline().rstrip().split()]
    
    d = {}
    for i in c:
      d[c] = d.get(c, 0) + 1
    
    for _, value in d.items():
      if value %2 != 0:
        out.append("YES")
    out.append("NO")
        
    
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    