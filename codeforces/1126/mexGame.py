import sys


if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [n, k] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    c = [int(i) for i in sys.stdin.readline().rstrip().split()]
    
    d = {}
    for i in c:
      d[i] = d.get(i, 0) + 1
    
    a = {}
    b = {}
        
    
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    