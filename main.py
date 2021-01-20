#Write your code below this line 👇
import math
def prime_checker(number):
  i=0
  #limit=int(math.floor(math.sqrt(number)))
  #print(limit)
  if number==2:
    print("It's a prime number.")
  else:
    for num in range(2,number):
      if number%num==0:
        i+=1
    print(f"i:{i}")
    if i>=1:
      print("It's not a prime number.")
    elif i==0:
      print("It's a prime number.")




#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)



