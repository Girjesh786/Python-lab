import numpy as np

# Given temperature readings
temperatures = np.array([32.5, 34.2, 36.8, 29.3, 31.0, 38.7, 23.1, 18.5, 22.8, 37.2])

# Identify hot days (temperature > 35 degrees Celsius)
hot_days = np.where(temperatures > 35)[0]

# Identify cold days (temperature < 5 degrees Celsius)
cold_days = np.where(temperatures < 5)[0]

# Output the results
print("Hot days):")
for day in hot_days:
    print(f"Day {day + 1}: {temperatures[day]} degrees Celsius")

print("\nCold days):")
for day in cold_days:
    print(f"Day {day + 1}: {temperatures[day]} degrees Celsius")
"""Output:
Hot days):
Day 3: 36.8 degrees Celsius
Day 6: 38.7 degrees Celsius
Day 10: 37.2 degrees Celsius

Cold days):
"""
