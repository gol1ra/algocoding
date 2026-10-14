import sys



def main(s):
  
  c = 1
  shorten = True
  lengthen = True
  for i in range(1, len(s)-1):
    if lengthen and (s[i-1] == s[i+1] and s[i] == s[i+1]):
      lengthen = False
      c += 1
    elif shorten and (s[i-1] == s[i+1] and s[i] != s[i+1]):
      shorten = False
      c += 1   
  return c

if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    s=  sys.stdin.readline().rstrip()
    
    out.append(main(s))
      
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    