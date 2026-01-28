import numpy as np

def sin(x):
    """
    input: float or numpy array
    output: sin(x)
    """
    return np.sin(x)
    
def cos(x):
    """
    input:float or numpy array
    output: cos(x)
    """
    return np.cos(x)

x_values = np.linspace(0, 2, 1000)
    #from 0 to 2 with 1000 entries

sin_values = sin(x_values)
cos_values = cos(x_values)

table_data = list(zip(x_values, sin_values, cos_values))

print(f"Generated {len(table_data)} entries.")

print(f"{'x':>10} {'sin(x)':>10}{'cos(x)':>10}")
print("-" * 35)

for i in range(10):
    x, s, c = table_data[i]
    print(f"{x:10.6f}{s:10.6f}{c:10.6f}")