import sys


if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [n] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    a = [int(i) for i in sys.stdin.readline().rstrip().split()]
    gaps = [abs(a[i]-a[i+1]) for i in range(n-1)]

    m = gaps[0]
    maxgaptourleft = [0]
    for i in range(1, n-1):
      if gaps[i-1] > m:
        m = gaps[i-1]
      maxgaptourleft.append(m)

    maxgaptourright = [0] * (n + 1)
    m = 0
    for i in range(n-2, -1, -1):
      if gaps[i] > m:
        m = gaps[i]
      maxgaptourright[i] = m

    g = gaps.index(max(gaps))
    ans = gaps[g]

    maxinternal = 0
    for r in range(g+1, n):
      if r > g+1:
        if 2*gaps[r-1] > maxinternal:
          maxinternal = 2*gaps[r-1]
      if maxinternal >= ans:
        break
      left_bound = abs(a[g] - 2*a[r])
      right_bound = abs(2*a[g+1] - a[r+1]) if r+1 < n else 0
      left_outside = maxgaptourleft[g]
      right_outside = maxgaptourright[r+1]
      cur = max(left_outside, left_bound, maxinternal, right_bound, right_outside)
      if cur < ans:
        ans = cur

    maxinternal = 0
    for l in range(g, -1, -1):
      if l < g:
        if 2*gaps[l] > maxinternal:
          maxinternal = 2*gaps[l]
      if maxinternal >= ans:
        break
      left_bound = abs(a[l-1] - 2*a[g]) if l > 0 else 0
      right_bound = abs(2*a[l] - a[g+1]) if g+1 < n else 0
      left_outside = maxgaptourleft[l-1] if l > 0 else 0
      right_outside = maxgaptourright[g+1]
      cur = max(left_outside, left_bound, maxinternal, right_bound, right_outside)
      if cur < ans:
        ans = cur

    out.append(str(ans))

  sys.stdout.write("\n".join(map(str, out)) + "\n")