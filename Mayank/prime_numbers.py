num = int(input("enter the number"))

for n in range(num+1):
  prime = True
  for m in range(2,n):
    # print(f"{n,m,n/m}")
    if n%m == 0:
      print(f"{n}is not a prime number")
      prime = False
      break
  if prime:   
   print(f"{n}is a prime number")
