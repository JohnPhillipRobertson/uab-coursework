import matplotlib.pyplot as plt
nums = "17.2 22.1 18.5 17.2 18.6 14.8 21.7 15.8 16.3 22.8 24.1 13.3 16.2 17.5 19.0 23.9 14.8 22.2 21.7 20.7 13.5 15.8 13.1 16.1 21.9 23.9 19.3 12.0 19.9 19.4 15.4 16.7 19.5 16.2 16.9 17.1 20.2 13.4 19.8 17.7 19.7 18.7 17.6 15.9 15.2 17.1 15.0 18.8 21.6 11.9"
nums = nums.split(" ")
nums = [float(i) for i in nums]
nums = sorted(nums)
print(nums)
# 11.9 12.0 13.1 13.3 13.4 13.5 14.8 14.8 15.0 15.2 15.4 15.8 15.8 15.9 16.1 16.2 16.2 16.3 16.7 16.9 17.1 17.1 17.2 17.2 17.5 17.6 17.7 18.5 18.6 18.7 18.8 19.0 19.3 19.4 19.5 19.7 19.8 19.9 20.2 20.7 21.6 21.7 21.7 21.9 22.1 22.2 22.8 23.9 23.9 24.1

# HOMEWORK 9

# Sample mean:
print("Sample mean: ", end="")
sm = sum(nums)/len(nums)
print(sm)
# 17.954

# Variance
print("Variance: ", end="")
var = sum([j**2 for j in [i - sm for i in nums]])/len(nums)
print(var)
# 9.768884

# Standard deviation
print("Standard deviation: ", end="")
sd = var**2
print(sd)
# 95.431094605456

# Median
print("Median: ", end="")
med = nums[len(nums)//2]
print(med)
# 17.6

# Five point summary
print("Five-point summary: ", end="")
fps = (min(nums), nums[len(nums)//4], med, nums[(len(nums)//4)*3], max(nums))
print(fps)
# (11.9, 15.8, 17.6, 19.8, 24.1)

# Interquartile range
print("Interquartile range: ", end="")
iqr = nums[(len(nums)//4)*3] - nums[len(nums)//4]
print(iqr)
# 4.0

# Print a histogram of values with intervals of .5.
print("Histogram: (See other window)",)
plt.hist(nums, rwidth=.5)
plt.show()
# Here it is.

# Does the histogram appear to be Normal? Skewed left? Skewed right? Bimodal?
print("It appears skewed left.")
# It appears skewed left.

# Are there any outliers?
print("There aren't any outliers.")
# There aren't any outliers.

# Should this have been a Jupyter Notebook?
