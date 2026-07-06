# House Robber
#  Problem statment:
#  -Given N number of houses along the street with some amount of money.
#  -Adjacent house cannot be stolen
#  -Find the maximum amount that can be stolen

# ex:-
#      (6)    (7)   (1)   (30)    (8)  (2)   (4)
#   Maximum Amount =41
#   House that are stolen = 7,30,4

#  option1= 6 + f(5)
#                    ----------->              Max (Option1, Option2)
#  Option = 0 +f(6)
#  Algorithm
#    maxValueHouse(house, currentHouse)
#         If currenthouse > length of house
#               return 0
#         Else
#              stealFirstHouse = currentHouse + maxValueHouse(houses, currentHouse+2)
#              skipFirstHouse = maxValueHouse(house, currentHouse+1)
#               return max(stealFirstHouse, skipFirstHouse)

def houseRobber(houses, currentIndex):
    if currentIndex >= len(houses):
        return 0
    else:
        stealFirstHouse = houses[currentIndex] + houseRobber(houses, currentIndex+2)
        skipFirstHouse = houseRobber(houses, currentIndex+1)
        return max(stealFirstHouse, skipFirstHouse)
    
houses = [6,7,1,30,8,2,4]
print(houseRobber(houses, 0))