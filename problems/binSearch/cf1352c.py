import sys

if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [n,k] = [int(i) for i in sys.stdin.readline().rstrip().split()]

    out.append(n*(k // (n-1)) + (k%(n-1) if k%(n-1) != 0 else -1))
  
  
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    