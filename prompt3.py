import numpy as np

def f(x):
	return x**3 + 8

def main():
	result = f(9)
	print(result)

	if result > 27:
		print("YAY!")
main()