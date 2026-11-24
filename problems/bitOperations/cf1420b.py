import sys



def main(v):
  c = 0
  
  d = {}
  for i in v:
    d[i] = d.get(i,0) +1

  for _, val in d.items():
    c += (val*(val - 1))//2
  
  return c

if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    sys.stdin.readline()
    v = [len(bin(int(i)))-2 for i in sys.stdin.readline().rstrip().split()]

    out.append(main(v))
  
  
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    