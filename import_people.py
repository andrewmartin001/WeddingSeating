import csv
import numpy
reader = csv.reader(open("input.csv", "rU"), delimiter=",")
x = list(reader)
result = numpy.array(x).astype("string")

#print result

#first row to labels
guest_names = result[0,1:]

N_GUESTS = len(guest_names)

print guest_names
#body to numbers, remove Xs and make symmetric

r_matrix = result[1:,1:]

r_matrix[r_matrix==''] = '0'
r_matrix[r_matrix=='X'] = '0'

#prioritise the twos...
r_matrix[r_matrix=='2'] = '4'

r_matrix = r_matrix.astype(numpy.float)
print r_matrix + r_matrix.T
