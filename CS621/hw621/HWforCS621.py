f = open("company_records.csv", "r")
r = [i.split(",") for i in f]
f.close()

# What is the budget of each department (total salary)?
deps = {}
for i in r:
    if i[2] == "Title":
        continue
    if i[3] not in deps.keys():
        deps[i[3]] = int(i[4])
    else:
        deps[i[3]] += int(i[4])
print("Budget of each department:\n" + str(deps))

# How many unique salaries the company has, what are they?
sals = set()
for i in r:
    if i[2] == "Title":
        continue
    sals.add(int(i[4]))
print("Unique salaries: " + str(len(sals)))

# Find the employees with the minimum and maximum salaries, display their full information
print("Employees with minimum and maximum salaries:")
for i in r:
    if i[2] == "Title":
        continue
    if int(i[4]) == min(sals):
        print(i)
        break
for i in r:
    if i[2] == "Title":
        continue
    if int(i[4]) == max(sals):
        print(i)
        break

# Which department has the highest budget?
print("Highest budget: " + str(max(deps, key=deps.get)))
print("Lowest budget: " + str(min(deps, key=deps.get)))

# Display the list of the departments with the total number of employees
deps = {}
for i in r:
    if i[2] == "Title":
        continue
    if i[3] not in deps.keys():
        deps[i[3]] = 1
    else:
        deps[i[3]] += 1
print("People in each department:\n" + str(deps))
