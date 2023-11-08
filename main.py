import matplotlib.pyplot as plt
import numpy as np
import random

if __name__ == "__main__":
    N = 30000
    x_yes = []
    y_yes = []
    x_no = []
    y_no = []

    for i in range(N):
        x = random.uniform(0, 4)  
        y = random.uniform(0, 4)  

        if (0 <= x <= 1 and 0 <= y <= 4) or (1 <= x <= 2 and 0 <= y <= 3) or (2 <= x <= 3 and 1 <= y <= 2) or (3 <= x <= 4 and 0 <= y <= 1):
            x_yes.append(x)
            y_yes.append(y)
        else:
            x_no.append(x)
            y_no.append(y)

    res = (len(x_yes) / N) * 16
    print(f'Площа дорівнює: {res:.2f}')  
    plt.scatter(x_yes, y_yes, color="blue", marker=".", s=10, label="Всередині")  
    plt.scatter(x_no, y_no, color="grey", marker=".", s=10, label="Зовні")  
    plt.xlabel("Вісь X")
    plt.ylabel("Вісь Y")
    plt.legend()  
    plt.show()
