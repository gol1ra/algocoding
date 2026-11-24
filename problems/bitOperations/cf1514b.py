import sys
  
if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [n,k] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    out.append(pow(n,k,10**9 + 7))
  
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    