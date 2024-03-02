stock={'apple':3,'mango':5,'banana':6}
item={'apple':100,'mango':80,'banana':60}
print("Items in stock",stock)
print("price of items",item)
count=0
while(True):
  x=input('Enter the key of items to be brought:' )
  if x in stock:
    count+=item[x]
    stock[x]=stock[x]-1
  else:
    print('item not found')
  print(count)
  print(stock)
  print(item)
  print('total price: ',count)