import sys

def main(a, x, k):
  n = len(a)

  isolated = []
    
  for i in range(n):
    if ((i == 0) or (a[i] - a[i - 1] > k)) and ((i == n - 1) or (a[i + 1] - a[i] > k)):
      isolated.append(a[i])

 
  pairs = 0
  i = 0
  m = len(isolated)
  while i + 1 < m:
    if isolated[i + 1] - isolated[i] <= 2 * k:
      pairs += 1
      i += 2
    else:
      i += 1

  return (m - pairs) <= x



if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [n, x] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    a = [int(i) for i in sys.stdin.readline().rstrip().split()]
    l = 1
    r = a[-1] - a[0]
    while l < r:
      m = (l+r) // 2
      if main(a, x, m):
        r = m
      else:
        l = m +1

    out.append(str(l))

  sys.stdout.write("\n".join(out))
    