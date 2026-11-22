import sys



def main(v):
  print(v)

  i = 0
  minc = 999999999999999
  empty = 0
  while empty < minc:
    c = 0
    empty = 0
    for s in v:
      if i >= len(s): c += 1; empty += 1
      else: c += 1 - int(s[i])

    if c < minc: minc = c

    i += 1
  return minc

if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    v = [bin(int(i))[2:][::-1] for i in sys.stdin.readline().rstrip().split()]

    out.append(main(v))
      
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    