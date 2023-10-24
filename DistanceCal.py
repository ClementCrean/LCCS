def caronly(km):
    cost = ((km * 0.2312)* 2)
    print(cost)
    return cost

def carpublic(km,cost):
    publicCost = ((cost + km * 0.2312)* 2)
    print(publicCost)
    return publicCost

def publiconly(costP):
   print((costP)* 2)
   return costP

transType = input("How did you travel to the course? \nA = Car only \nB= Car + Public Transport \nC = Public Trans \n Answer: ")
if transType == 'A':
    cardist = float(input("Enter kms travelled: "))
    caronly(cardist)
    
elif transType == 'B':
    carpubcost = float(input("Enter cost of train and taxi: "))
    carpublic(carpubcost,cardist)
    
elif transType == 'C':
    pubcost = float(input("Enter cost of the taxi: "))
    publiconly(pubcost)
