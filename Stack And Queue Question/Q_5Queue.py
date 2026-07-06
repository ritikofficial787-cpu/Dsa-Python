#Animal shelter.
class AnimalSeletr():
    def __init__(self):
        self.cat=[]
        self.dogs=[]

    def Enqueue(self,Animals,Type):
        if Type=='Cat':
            self.cat.append(Animals)
        else:
            self.dogs.append(Animals)

    def dequeuecat(self):
        if len(self.cat) == 0:
            return None
        else:
            cat = self.cat.pop(0)
            return cat
            
    def dequeuedog(self):
        if len(self.dogs)==0:
         return None
        else:
            dogs=self.dogs.pop(0)
            return dogs
        
    def any(self):
        if len(self.cat) ==0:
            result =self.dogs.pop()
        else:
            result=self.cat.pop(0)
            return result
        

customQueue=AnimalSeletr()
customQueue.Enqueue('Cat1', 'Cat')
customQueue.Enqueue('Cat2', 'Cat')
customQueue.Enqueue('Dog1', 'Dog')
customQueue.Enqueue('Cat3', 'Cat')
customQueue.Enqueue('Dog2', 'Dog')
print(customQueue.dequeuecat())
print(customQueue.dequeuecat())
print(customQueue.any())