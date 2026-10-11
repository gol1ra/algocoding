import sys

def main(vc, hc):
  matrix = [[0] * hc[-1] for _ in range(vc[-1])]

  for i in range(len(vc) - 1):
    for j in range(len(hc) - 1):
      H = vc[i+1] - vc[i]
      W = hc[j+1] - hc[j]
      area = H * W
      forbidden = set()

      if i > 0:
        for b in range(W):
          forbidden.add((matrix[vc[i]-1][hc[j]+b] - 1 - b) % area)
      if j > 0:
        for a in range(1, H):
          forbidden.add((matrix[vc[i]+a][hc[j]-1] - 1 - a * W) % area)

      if i > 0 and j > 0:
        forbidden.add((matrix[vc[i]][hc[j]-1] - 1) % area)

      shift = -1
      for k in range(area):
        if k not in forbidden:
          shift = k
          break

      if shift == -1:
        return "-1"

      for a in range(H):
        for b in range(W):
          matrix[vc[i]+a][hc[j]+b] = ((a * W + b + shift) % area) + 1

  out_lines = []
  for row in matrix:
    out_lines.append(" ".join(map(str, row)))

  return "\n".join(out_lines)


if __name__ == "__main__":
  t = int(sys.stdin.readline().rstrip())
  out = []

  for _ in range(t):
    m, n, v, h = map(int, sys.stdin.readline().split())

    vc = [0]
    hc = [0]

    if v != 0:
      vc += list(map(int, sys.stdin.readline().split()))

    if h != 0:
      hc += list(map(int, sys.stdin.readline().split()))

    vc.append(m)
    hc.append(n)

    out.append(main(vc, hc))

  sys.stdout.write("\n".join(out) + "\n")