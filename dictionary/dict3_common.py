x=int(input("Enter the no of input in dict1: "))
D1={}
for i in range(x):
  y=input("Enter the key: ")
  z=input("Enter the value: ")
  D1.update({y:z})

x1=int(input("Enter the no of input in dict1: "))
D2={}
for i in range(x):
  y1=input("Enter the key: ")
  z1=input("Enter the value: ")
  D2.update({y:z})
print(D1)
print(D2)
for i in D1:
  if i ==i in D2:
    print(i)
