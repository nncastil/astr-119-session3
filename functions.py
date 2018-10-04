import numpy as np	#library name
import sys			#gives access to info from operating system to command line

#define function that returns a value
def expo(x):
	return np.exp(x)	#returns the np e^x function
	
#define a subroutine that does not return a value
def show_expo(n):
	for i in range(n):			#i=[0, n-1]
		print(expo(float(i)))	#calls the expo function, e^float(i)
		
#define a main function
def main():
	n = 10	#default function for n
	
	#check if there is a command line argument
	if(len(sys.argv)>1):		#len tells length of the array, sys.argv
		n = int(sys.argv[1])	#converting command line to integer = n
		
	show_expo(n)	#calls expo subroutine
	
	
#run the main function
if __name__ == "__main__":
	main()