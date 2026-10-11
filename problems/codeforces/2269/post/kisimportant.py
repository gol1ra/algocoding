import sys

if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [n, k] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    vals = [int(i) for i in sys.stdin.readline().rstrip().split()]
    b,t = min(k ,n -k+1), max(k, n-k+1)
    c = len(vals) - k
    s = 0
    while c > 0:
      if vals[b] > vals[t]:
        s += vals[b]
        vals[b] = 0
        b+=1
        t += 1
        
        
    
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    