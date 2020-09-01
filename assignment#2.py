import re
import statistics
s = input("Anna lista numeroita: ")
result = [int(d) for d in re.findall(r'-?\d+', s)]

#sum
print ("Sum:    ",sum(result))

#mean
mean1=str(statistics.mean(result))
mean1=float(mean1)
print ("Mean:   ",str(round(mean1, 1)))

#median
median1=str(statistics.median(result))
median1=float(median1)
print ("Median: ",str(round(median1, 1)))

