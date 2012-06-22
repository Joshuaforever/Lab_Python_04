#1
groceries=['bananas','strawberries','apples','bread']
groceries.append('Champagne')
print groceries
#1b
groceries.remove('bread')
print groceries
#1c
groceries=['bananas','strawberries','apples','bread']
groceries.sort()
print groceries

#2.a. I will use a list.
#2b
store={'Apples':'7.3','Bananas':'5.5','Bread':'1.0','Carrots':'10.0','Champagne':
       '20.90','Strawberries':'32.6'}
print store
#2c
store={'Apples':'7.3','Bananas':'5.5','Bread':'1.0','Carrots':'10.0','Champagne':
       '20.90','Strawberries':'32.6'}
store['Strawberries']=63.43
print store
#2d  
store['Chicken']=6.5

#3a. A list will be best for this because prices of goods are always gonna change.
#3b
in_stock={'Apples':'7.3','Bananas':'5.5','Bread':'1.0','Carrots':'10.0','Champagne':
       '20.90','Strawberries':'32.6'}
#Tupple
#3c
always_in_stock=tuple(in_stock)
#3d
print "Come to shoprit! We always sell:"
print always_in_stock,""
#4a.They could use dictionary.
#4b.
def binary_search(lb=0.5,ub=1.5):
    while lb<ub:
        mid=(lb+ub)/2
        midval=a[mid]
        if midval<x:
            lb=mid+1
        elif midval>x:
            ub=mid-1
        else:
            return mid

