#A set is a non index collection.
Colors={"Yellow","Blue","Red"}
print(type(Colors))
print(dir(Colors))
print("Yellow" in Colors)
Colors.remove("Blue")
print(Colors)
Colors.clear()
print(Colors)
del Colors
print(Colors)

