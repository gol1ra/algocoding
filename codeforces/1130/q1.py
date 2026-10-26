import sys



def main(d,n,k):
  swapfrom = -1
  available = set([i for i in range(n-k+1)])
  for i in range(0,n-k+1):
    if d[i] > n-k and swapfrom==-1:
      swapfrom = d[i] +1
    else:
      available -= {d[i]}
      
  if swapfrom == -1:
    return '-1'
  return f'{min(available)+1} {swapfrom}'



if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [n, k] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    vals = [int(i) for i in sys.stdin.readline().rstrip().split()]
    c = 0
    d = {}
    for i in range(n):
      d[vals[i]] = i
      
    
    out.append(main(d,n,k))
      
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    