import sys


if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    n = int(sys.stdin.readline().rstrip().split())
    c = [int(i) for i in sys.stdin.readline().rstrip().split()]
    check = [False]*n
    
    currmax = c[0]
    currindex = 0
    for i, k in enumerate(c[1:], 1):
      if k == currmax:
        for j in range(currindex, i+1):
          check[i] = True 
      if k > currmax:
        currmax=k
        currindex = i
        
        
    currmax = c[-1]
    currindex = 0
    for i, k in enumerate(c[1:][::-1], 1):
      if k == currmax:
        for j in range(len(c) - i-1,len(c) -currindex):
          check[i] = True 
      if k > currmax:
        currmax=k
        currindex = i
      
      
      
      
    
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    