import sys


if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [n, k] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    v = sum([int(i)%2 for i in sys.stdin.readline().rstrip().split()])
    r = sum([int(i)%2 for i in sys.stdin.readline().rstrip().split()])
    #oddcount
    
    if k%2 == 1: 
      if v <= r:
        out.append('YES')
      else:
        out.append('NO')
    else:
      if v >= r:
        out.append('YES')
      else:
        out.append('NO')
    
    
      
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    