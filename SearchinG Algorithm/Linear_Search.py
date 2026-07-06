#Linear Search:-
#  -Create function with two parameters which are an array and a value.
#  -Loop through the array and check if the current array element is equal to the value.
#  -If it is return the index at which the element is found.
#  -If the value is never found return -1.


def linearSearch(array,value):
    for i in range(len(array)):
        if array[i]==value:
            return i
    return -1


print(linearSearch([20,40,30,50,60,90,80], 510))