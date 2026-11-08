import sys

def ask(l, r):
  print(f"? {l} {r}", flush=True)
  x = int(sys.stdin.readline())
  if x == -1:
    sys.exit(0)
  return x


if __name__ == "__main__":
  t = sys.stdin.readline()
  
  for _ in range(int(t)):
    n = int(sys.stdin.readline())

    total_ones = ask(1, n)
    
    if total_ones == 0 or total_ones == n:
      print("! NO", flush=True)
      continue
    
    if ask(1,total_ones) == total_ones:
      print("! NO", flush=True)
      continue
    
    print("! YES", flush=True)