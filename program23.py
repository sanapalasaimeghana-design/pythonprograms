n=int(input("enter n value"))
f=0
for i in range(1,n+1):
	if n%i==0:
		f=f+1
if f==2:
	print("the given no is prime number")

else:
	print("the given no is not a prime number")

	
		