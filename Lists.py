#This file contains fundamental notions about lists.
Demolist1=[1, "John", True, 1,8, [1,2,3,4]]
print(Demolist1)
Demolist2=list((1, "John", True, 1,8, [1,2,3,4]))
print(Demolist2)
Demolist3=list(range(0,10))
print(Demolist3)
print(len(Demolist1))
print(Demolist1[5])
print("John" in Demolist1)
Demolist1[4]=False
print(Demolist1)
Demolist1.append("Juan") #append just works with one argument.
print(Demolist1)
Demolist1.extend([7,8,9])
print(Demolist1)
Demolist1.insert(1,2)
print(Demolist1)
Demolist1.insert(len(Demolist1),"Carlos")
print(Demolist1)
Demolist1.pop()
print(Demolist1)
Demolist1.remove("Juan")
print(Demolist1)
Demolist1.pop(0)
print(Demolist1)
Demolist3.reverse() #To order, use sort
print(Demolist3)