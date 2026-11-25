import sys


p = [1, 2, 4, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 262144, 524288, 1048576, 2097152, 4194304, 8388608, 16777216, 33554432, 67108864, 134217728, 268435456, 536870912]
def main(a):
  

  # print(a)
  i = 0
  vals = {}
  flag = True
  while flag:
    c = 0
    flag = False
    for v in a:
      if i < len(v):
        c+= int(v[i])
        flag = True
    vals[i] = c
    # print(i, flag)
    i +=1
    
  # print(vals)
  
  flag = True
  r = 0
  while flag:
    flag = False
    num = 0
    for j in range(i):
      if vals[j] > 0:
        num += p[j]
        vals[j] -= 1
        flag = True
    # print(f'---{num}----{vals}')
    r += num**2
  
  return r
      

if __name__ == "__main__":
  sys.stdin.readline()
  a = [bin(int(i))[2::][::-1] for i in sys.stdin.readline().rstrip().split()]
  
  
  sys.stdout.write(str(main(a)) + "\n")
    