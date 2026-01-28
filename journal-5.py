import numpy as np

def main():
    x_values = np.linspace(0, 2, 1000)
    
    y_values = np.sin(x_values)

    print(f"{'x':>10} | {'sin(x)':>10}")
    print("-" * 23)
    
    for x, y in zip(x_values, y_values):
        print(f"{x:10.6f} | {y:10.6f}")

if __name__ == "__main__":
    main()