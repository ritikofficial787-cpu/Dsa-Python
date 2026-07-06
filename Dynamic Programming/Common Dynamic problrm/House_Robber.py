#Top Down Approach



def houseRobberTD(houses, currentIndex, tempdict):
    if currentIndex >= len(houses):
        return 0
    else:
        if currentIndex not in tempdict:
            stealFirstHouse = houses[currentIndex] + houseRobberTD(houses, currentIndex+2, tempdict)
            skipFirstHouse = houseRobberTD(houses, currentIndex+1, tempdict)
            tempdict[currentIndex]=max(stealFirstHouse, skipFirstHouse)
        return tempdict[currentIndex]
        
houses = [6,7,1,30,8,2,4]
print(houseRobberTD(houses,0,{}))

#Bottom Up Approach
def houseRobberBU(houses , currentIndex):
    tempARR = [0] * (len(houses)+2)
    for i in range(len(houses)-1, -1, -1):\
       tempARR[i]=max(houses[i]+tempARR[i+2], tempARR[i+1])
    return tempARR[0]

print(houseRobberBU(houses,0))