import numpy as np
from tabulate import tabulate
from astropy.table import Table

def main():
	x = np.linspace(0, 2, 1000)		# 0 to 2 in 1000 step
	y = np.sin(x)

	table_data = [(a,b)for a,b in zip(x,y)]

	table_headers = ["x", "sin(x)"]

	python_table = tabulate(table_data[:10], tablefmt="grid", headers=table_headers, floatfmt=".6f")
	print("Preview of first 10 rows:")
	print(python_table)

	with open("sin_table.txt", "w") as f:
		f.write(f"{'x':>12}{'sin(x)':>12}\n")
		f.write("-" * 25 + "\n")
		for a, b in table_data:
			f.write(f"{a:12.6f}{b:12.6}\n")

	print("Full table saved to sin_table.txt")


if  __name__ == "__main__":
	main()