#1. Create an array and traverse
from array import *
arr1=array('i',[1,2,3,4,5,6])  
for i in arr1:
 print (i)
#2. Access individual ements through indexes
print("Question2")
print(arr1[0])

#3. Append any value to the array using append() method
print("Question3")
arr1.append(6)
print(arr1)
#4. Insert value in an array usinf insert()method
print("Question4 ")
arr1.insert(0,11)
print(arr1)

#5. Extend python array using extend() method
print("Question5")
my_array=array('i',[15,16,17])
arr1.extend(my_array)
print(arr1)
#6. Add items from list into array using fromlist() method
print("Question6")
my_list=[20,21,22,23]
arr1.fromlist(my_list)
print(arr1)
#7. Remove ant array element using remove() method.
print("Question7")
arr1.remove(20)
print(arr1)
#8. Remove last array element using pop() method.
print("Question8")
arr1.pop()
print(arr1)
#9. Fetch any element through its index using index() method
print("Question9")
print(arr1.index(11))
#10 Reverse a python array using reverse() method.
print("Question10")
arr1.reverse()
print(arr1)
#11.Get array buffer infromation thruogh buffer_info() method 
print("Question11")
array2=arr1.buffer_info()
print(array2)
#12.Check for number of occurences of an element using count() method
print("Qestion12")
arr1.append(22)
print(arr1.count(22))
print(arr1)
#13.Convert array to string using tostring() method
print("Question13")
# Modern fix: Use .tobytes() instead of .tostring()
strTemp = arr1.tobytes()
print(strTemp)
ints= array('i')
ints.frombytes(strTemp)
print(ints)
#14.Convert array to a python list with same elements using tolist() method
print("Question14")
print(arr1.tolist())
#15.Append a string to char array using fromstring() method
#15. Append a string to char array using frombytes() / fromunicode() method
print("Question15")

# 1. Create a character (Unicode) array
char_array = array('u', ['H', 'e', 'l', 'l', 'o'])

# 2. Append a string to it using .fromunicode() 
# (Or use .frombytes() if you are working with standard byte arrays)
char_array.fromunicode(" World")

print(char_array)
#16.Slice Elements from array
print("Question16")
print(arr1[2:5])

