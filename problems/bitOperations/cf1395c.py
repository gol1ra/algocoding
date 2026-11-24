import sys



def main(a,b):
  matrix = [[i & j for j in b] for i in a]
  
  def check(i):
    for r in matrix:
      flag = False
      for col in r:
        if i|col == i:
          flag = True
          break
      if not flag: return False
    return True
  i = 0
  while i<512:
    if check(i): return i
    i+=1

if __name__ == "__main__":
  # [n,m] = [int(i) for i in sys.stdin.readline().rstrip().split()]
  sys.stdin.readline()
  a = list(set([int(i) for i in sys.stdin.readline().rstrip().split()]))
  b = list(set([int(i) for i in sys.stdin.readline().rstrip().split()]))
  
    
      
  
  
  sys.stdout.write(str(main(a,b)) + "\n")
    