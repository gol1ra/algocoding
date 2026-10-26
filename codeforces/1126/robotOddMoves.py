import sys





if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [a, b] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    if b > a+1:
      out.append(-1)
    else:
      if b % 2 == 0:
        out.append(a if a % 2 == 0 else a+1)
      else:
        out.append(a if a%2 == 1 else a+1)
        
        
    
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    