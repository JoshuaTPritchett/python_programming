import math
import unittest
"""
	Bruh here is a fun test of basic python skills
"""



def convert_binary(num):
	test = []
	b = num
	while b > 0:
		test.append(b%2)
		b = b/2
	test.reverse() #little edian format	
	ret_value = ''.join(str(e) for e in test)
	return ret_value


def convert_binary_decimal(str_num):
	a = 0
	twos_power = 0
	#convert back to big endian
	for s in str_num[::-1]:
		if s == '1':
			a = a + pow(2 ,twos_power)
		twos_power = twos_power  + 1
	return a


def convert_binary_octal(str_num):
	a = 0
	temp_place = 1
	temp1 = str_num
	n = 3
	print n
	for i in range(len(str_num), 0, -n):
		if i - n > 0:
			print str_num[i-n:i]
		else:
			print str_num[i - (i % n): i]


	"""list_A = 	[str_num[i:i-3] for i in range(len(str_num) - 1, -1, -3)]
	print list_A
	#shit this is going to be soooo inefficient
	#whoa, what the hell is this next line?!?! wizardry.....
	for i in range(len(list_A) -1 , -1, -1):
			print i
			temp_list = list_A[i]
			print 'PRINTING LIST'
			print list_A[i]
			twos_power = 0
			temp_num = 0
			for bit in temp_list[::-1]:
					print bit
					if bit == '1':
							print 'HERE IS TEMP NUM'
							temp_num = temp_num + pow(2, twos_power)
					twos_power = twos_power + 1
			a = a + temp_num
			print a
			a = a + (pow(10, temp_place)) 
			print a
		"""	
	#print a


value = 8
print(value)

b_str = convert_binary(value)

d_num = convert_binary_decimal(b_str)
print (d_num)

convert_binary_octal(b_str)


#Shit I suck lemme practice that slicing stuff....
"""
s = 'Don Quijote'
print s[4:8] # from 4-8
print s[4:] # to end of string
print s[:4] # 1-4
print s[:] #why? well because...
print s[:6] + s[6:] #this is trill but liek ....
print s[-3:-1]
print s[4:8:1] #from 4-8 skip by 1
print s[4:8:2] #from 4-8 skip by 2
print s[8:4:-1] # 8-4 going by 1
print s[4::-1] #from 4-1 going by -1 going backwards
print s[:4:-1] #end of string to 4 -1 going backwards
"""
#LETS PRACTICE HERP
#print s[len(s): -3:1]
#print s[0:1]
#print s[6:9]
#print s[len(s):-3:1]
#GOT IT
