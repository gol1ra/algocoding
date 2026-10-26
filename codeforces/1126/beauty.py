import sys


def beautiful(a):
  n = len(a)
  left = [-1] * n
  right = [n] * n
  stack = []

  for i in range(n):
    while stack and a[stack[-1]] <= a[i]:
      stack.pop()
    if stack:
      left[i] = stack[-1]
    stack.append(i)

  stack = []

  for i in range(n - 1, -1, -1):
    while stack and a[stack[-1]] <= a[i]:
      stack.pop()
    if stack:
      right[i] = stack[-1]
    stack.append(i)

  groups = {}
  for i, x in enumerate(a):
    key = (x, left[i], right[i])
    if key not in groups:
      groups[key] = [i, i]
    else:
      groups[key][1] = i

  diff = [0] * (n + 1)

  for l, r in groups.values():
    if l < r:
      diff[l] += 1
      diff[r + 1] -= 1

  cover = 0
  for i in range(n):
    cover += diff[i]
    if cover == 0:
      return False

  return True


def solve(a):
  n = len(a)
  piller_operations = []

  if beautiful(a):
    return piller_operations

  x = max(a[0], a[-1])

  if a[0] != a[-1] and max(a) == x:
    piller_operations.append((1, x))
    a[0] = x
    return piller_operations

  if a[0] == a[-1]:
    bad = [i for i in range(1, n - 1) if a[i] > a[0]]

    if len(bad) == 1:
      i = bad[0]
      piller_operations.append((i + 1, a[0]))
      return piller_operations

  x = max(a)

  if a[0] != x:
    piller_operations.append((1, x))

  if a[-1] != x:
    piller_operations.append((n, x))

  return piller_operations


if __name__ == "__main__":
  input = sys.stdin.readline
  t = int(input())
  out = []

  for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))

    piller_operations = solve(a)

    out.append(str(len(piller_operations)))
    for i, x in piller_operations:
      out.append(f"{i} {x}")

  sys.stdout.write("\n".join(out) + "\n")