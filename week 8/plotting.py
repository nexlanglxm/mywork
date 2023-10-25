import numpy as np
minSalary = 20000
maxSalary = 80000
numberofEntries = 10

salaries = np.random.randint(minSalary, maxSalary, numberofEntries)
print (salaries)

salariesPlus = salaries + 5000
print (salariesPlus)