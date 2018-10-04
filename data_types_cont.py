#strings

s = "I am a string."
print(type(s))					#will say "str"

#Boolean

yes = True						#Boolean True
print(type(yes))

no = False						#Boolean False
print(type(no))

#List -- ordered and changeable

alpha_list = ["a", "b", "c"]	#list initialization
print(type(alpha_list))			#says "list"
print(type(alpha_list[0]))		#says "string"
alpha_list.append("d")			#adds "d" to end of list
print(alpha_list)				#prints list

#Tuple -- ordered and UNchangeable

alpha_tuple = ("a", "b", "c")	#tuple initialization
print(type(alpha_tuple))		#says "tuple"

try:							#attempt to change the tuple
	alpha_tuple[2] = "d"		#will raise TypeError
except TypeError:				#when we get TypeError...
	print("We can't add elements to tuples!")
print(alpha_tuple)				#prints tuple