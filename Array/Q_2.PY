#Find pairs in an array whose sum is equal to a given number
#Write a program to find all pairs of intgers whose sum is equal to given number
#[2,6,3,9,11]  9-------->[6,3]
#Does array conatain only +ve or -ve number?
#What if the same pair repeats twice, should we print every time?
#If the reverse of the pair is accepetable eg. can we print both(4,1) and (1,4) if the given sum is 5.
#Do we need to print only distinct pairs?does(3,3) is a valid pair of forgiven sum of 6?
#How big is the array


def findpairs(array,sum):
    for i in range(len(array)):
        for j in range(i+1,len(array)):
            if array[i]+array[j]==sum:
                print(array[i],array[j])
arr=[2,6,3,9,11,8,1,4,5]
findpairs(arr, 9)