#Importing re module for regular expression
import re 
input_string = "$180,240/y"

# printing original string 
print("The original string : " + input_string)

#Importing regular expression
output_int = re.sub("\D", "", input_string)

# print result
print("The numbers list is :" + str(output_int))
