#!/usr/bin/python3
#function that takes n arguments and returns 1 argument

def hello(v1,v2):
	t1=v1+' '+v2
	return t1

def main():
	var1='babu'
	var2='bhaiya'
	var3=hello(var1,var2)
	print(var3)

if __name__=='__main__':
	main()
