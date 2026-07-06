#Zero One Knapsack Problem:-
#Problem Statement:-
#    -Given the weights and profit of N items
#    -Find the maximum profit within given capacity of C
#    -Items cannot be broken
#  ex: 1
#   Mango(wt=3, profit=31), Apple(wt=1, profit=26), Orange(wt=2, profit=17), Banana(wt=5, profit=72)
#   Knapsack Capacity : 7
# -Answer combination:-
#        -Mango + Apple + Orange = wt=6, profit=74
#        -Orange + Banana = wt=7, profit=89
#        -Apple + Banana = wt=6, profit=98
#subproblems:
#  option1=31+f(2,3,4)
#                     --------------------> Max(option1, option2)
#  option2 = 0 +f(2,3,4)

#Algorithm  :
#   zoknapSack(items, capacity, currentIndex):
#      If capacity<=0 or currentIndex<0 or currentIndex>len(profit)
#           return 0
#      Elif   currentItemWeight <= capacity
#            profit1 = currentItemProfit + zoKanpsack(items, capacity- currentItemsWeight,nextItem)
#            profit2 = zoKnapsack(items, capacity-currentItemsWeight, nextItem)
#            return max(profit1, profit2)
#      Else
#         return 0

class Items:
    def __init__(self, profit, weight):
        self.profit=profit
        self.weight=weight

def zoKnapSack(items, capacity, currentIndex):
    if capacity <=0 or currentIndex <0 or currentIndex >= len(items):
        return 0
    elif  items[currentIndex].weight <=capacity:
        profit1= items[currentIndex].profit + zoKnapSack(items, capacity-items[currentIndex].weight, currentIndex+1)
        profit2 = zoKnapSack(items, capacity, currentIndex+1)
        return max(profit1, profit2)
    else:
        return 0
    
mango = Items(31,3)
apple = Items(26,1)
orange =Items(17,2)
banana = Items(73, 5)

items = [mango, apple, orange, banana]

print(zoKnapSack(items, 7, 0))