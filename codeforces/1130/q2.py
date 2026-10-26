import sys

if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    n = int(sys.stdin.readline().rstrip())
    s1 = sys.stdin.readline().rstrip()
    s2 = sys.stdin.readline().rstrip()
    
    k = s1.count('f') - s2.count('f')
    if k > 0:
      i = 0
      while i < n and k>=2:
        if s1[i] == 'f' and s1[i+1] == 'f':
          i+=1
          k-=2
        i+=1
    elif k < 0:
      k = abs(k)
      i = 0
      while i+1 < n and k>=2:
        if s2[i] == 'f' and s2[i+1] == 'f':
          i+=1
          k-=2
        i+=1
    out.append(k)
      
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    