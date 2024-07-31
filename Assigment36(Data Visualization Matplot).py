#Create a bar chart to represent monthly expenses in different spending categories and give your conclusion.
import matplotlib.pyplot as plt

# Data
categories = ['Rent', 'Groceries', 'Utilities', 'Entertainment', 'Transportation']
expenses = [1200, 400, 200, 150, 250]

# Create the bar chart
plt.figure(figsize=(10, 6))
plt.bar(categories, expenses, color=['blue', 'green', 'red', 'purple', 'orange'])
plt.xlabel('Spending Categories')
plt.ylabel('Monthly Expenses (in dollars)')
plt.title('Monthly Expenses by Category')
plt.grid(True, linestyle='--', alpha=0.6)

# Display the chart
plt.show()
"""
Conclusion:
Rent is the highest expense category, with monthly expenses reaching $1200.
This is significantly higher than any other category, indicating that rent
is a major portion of the monthly budget.
"""
