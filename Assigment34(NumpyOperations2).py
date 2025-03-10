#Calculate the profit made by a company
import numpy as np

revenue = np.array([10000, 12000, 11000, 10500])
expenses = np.array([4000, 5000, 4500, 4800])

profit = revenue - expenses

print("Profit:", profit)

"""Output:
    Profit: [6000 7000 6500 5700]
    """
