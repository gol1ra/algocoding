import sys
import math

if __name__ == "__main__":
  s = sys.stdin.readline().rstrip()
  
  map = {
    'B': 0,
    'C': 2,
    'S': 1
  }
  
  # bread, suausage, cheese   nums in order
  recipe = [0,0,0]
  
  for i in s:
    recipe[map[i]] += 1
 
  kitchen = [int(i) for i in sys.stdin.readline().rstrip().split()]
  prices = [int(i) for i in sys.stdin.readline().rstrip().split()]
  p = int(sys.stdin.readline().rstrip())
  
  def valid(n):
    spent = 0
    for i in range(3):
        spent += max(0, n*recipe[i] - kitchen[i]) * prices[i]
    return spent <= p
  
  def main():
    lo = min([kitchen[i]//recipe[i]  for i in range(3) if recipe[i] != 0])
    hi = lo + p + 1    
    mid = (lo + hi+1)//2
    
    
    while lo != hi:
      if valid(mid):
        lo = mid
      else:
        hi = mid -1
        
      mid = (lo + hi+1)//2
      
    return mid
  
  
  
  sys.stdout.write(str(main()) + "\n")
    