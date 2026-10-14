import sys



def main(c,s):
  if c<=s:
    return -1
  else:
    return min(c-s, s)



if __name__ == "__main__":
  t = sys.stdin.readline().rstrip()
  out = []
  for _ in range(int(t)):
    [c, s] = [int(i) for i in sys.stdin.readline().rstrip().split()]
    
    out.append(main(c,s))
      
  sys.stdout.write("\n".join(map(str, out)) + "\n")
    