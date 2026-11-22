

import sys



def main(d):
  pass
  
if __name__ == "__main__":
  
  [n, m, k] = [int(i) for i in sys.stdin.readline().rstrip().split()]
  v = []
  for _ in range(m+1):
    v.append(int(sys.stdin.readline().strip()))
  c = 0
  for i in range(m):
    # print(f"-{bin(v[i] ^ v[m])} {(v[i] ^ v[m])}")
    if (v[i] ^ v[m]).bit_count() <= k:
      c +=1

  # print('------------------')
  sys.stdout.write(f"{c}\n")
    