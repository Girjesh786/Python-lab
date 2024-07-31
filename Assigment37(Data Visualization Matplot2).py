#Visualize the daily temperature changes over time in a city and give your conclusion
import matplotlib.pyplot as plt

# Data
days = list(range(1, 32))
temperature = [65, 68, 70, 72, 75, 76, 78, 80, 81, 79, 75, 72, 70, 68, 67, 69, 70, 73, 75, 76, 78, 80, 81, 82, 83, 82, 80, 78, 76, 74, 71]

# Create the line chart
plt.figure(figsize=(12, 6))
plt.plot(days, temperature, marker='o', linestyle='-', color='b')
plt.xlabel('Days')
plt.ylabel('Temperature (°F)')
plt.title('Daily Temperature Changes Over Time')
plt.xticks(days, rotation=45)
plt.grid(True, linestyle='--', alpha=0.6)

# Display the chart
plt.show()
"""
Conclusion:
The temperature shows a cyclical pattern, with two clear peaks and two troughs
There is an overall upward trend in the first half of the month, followed
by a downward trend and then another upward trend towards the end of the month.
"""
