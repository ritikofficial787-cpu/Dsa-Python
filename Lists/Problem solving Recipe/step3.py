"""
Step 3 - Break It down

 Write out the steps that you need to take
"""

#Write a functio with takes in a string and returns count of each character in the string

charcount= ("I am Ritik")
 # I:1
 # A:1
 # M:1
 # R:1
 # I:2
 # T:1
 # K:1

def charcount(string):
   # declare an object to return at the end
   result = {}
   #loop over the string, for each character
   for i in string:
   # if the char is letter and it is in out object, add one to value
     if i in result:
      result[i] += 1
   # if the char is letter and it is not in our object add that char to our object and set value to 1
     else:
      result[i] = 1
   # return something
   return result

print(charcount("I am rRitik"))