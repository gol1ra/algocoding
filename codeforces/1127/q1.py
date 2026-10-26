import sys





if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [n] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    vals = [int(i) for i in sys.stdin.readline().rstrip().split()][::-1]
    pos = 0
    for v in vals:
      pos += 2*(v-pos)
    out.append(int(pos/2))
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    