import numpy as np

#integers

i = 10	#integer
print(type(i))	#tells data type of i

a_i = np.zeros(i,dtype=int)	#declares an array of integers
print(type(a_i))			#will return ndarray
print(type(a_i[0]))			#will return int64

#floats

x = 119.0		#floating point number
print(type(x))	#prints out data type of x

y = 1.19e2		#scientific notation of 119
print(type(y))	#prints out data type of y

z = np.zeros(i,dtype=float)	#declares array of floats
print(type(z))				#will return ndarray
print(type(z[0]))			#will return float64