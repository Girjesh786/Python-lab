# Write a Python script to concatenate the following dictionaries to create a new one.
dic1 = {1: 10, 2: 20}
dic2 = {3: 30, 4: 40}
dic3 = {5: 50, 6: 60}
# Concatenating dictionaries
result = {}
for d in (dic1, dic2, dic3):
    result.update(d)
# Printing the result
print(result)
#Output: {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
