

import sys



def main(d):
  
  m = 0
  flag = False
  flag1 = False
  for i in d:
    if i == 0:
      return "Brain Melt"
    
    if i > 1:
      if flag:
        flag1 = True
      else:
        m = i
        flag = True
    
  if m == len(d)-1 and not flag1:
    return 2
  return "Many"
  
  
if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [n, m] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    vals = [[int(i) for i in sys.stdin.readline().rstrip().split()] for _ in range(m)]
    
    degs = [0 for _ in range(n)]
    for [a,b] in vals:
      if a!=b:
        degs[a-1] += 1
        degs[b-1] += 1
    
    out.append(main(degs))
    
      
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    