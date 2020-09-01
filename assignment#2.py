import re
import statistics
s = input("Anna lista numeroita: "s)
result = [int(d) for d in re.findall(r'-?\d+', s)]

#sum
print ("Sum:    ",sum(result))

#mean
print ("Mean:   ",str(round(statistics.mean(result), 1)))

#median
print ("Median: ",str(round(statistics.median(result), 1)))

