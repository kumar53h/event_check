#!/usr/bin/python3
import pdb
#pdb.set_trace()

def main():
	a=int(input('First Number\n'))
	b=int(input('Second Number\n'))
	result=lesser_of_two_evens(a,b)
	print(result)

def even_checker(a,b):
	if a%2==0 and b%2==0:
		return True
	else:
		return False

def lesser_of_two_evens(a,b):
	if even_checker(a,b)== True:
		if a<b:
			return a
		else:
			return b
	else:
		if a>b:
			return a
		else:
			return b

if __name__=='__main__':
	main()

