#methods are subroutines that allow us tho have information about variables, or make changes on it. Fir instance, type()
#Here are presented the main methods for strings.
Example_Variable=("John Benet")

print(dir(Example_Variable))
print(Example_Variable.upper())
print(Example_Variable.lower())
print(Example_Variable.swapcase())
print(Example_Variable.capitalize())
print(Example_Variable.replace("oh","ua"))
print(Example_Variable)
print(Example_Variable.count("h"))
print(Example_Variable.startswith("J"))
print(Example_Variable.endswith("m"))
print(Example_Variable.split())
print(Example_Variable.find("B"))
print(len(Example_Variable))
print(Example_Variable.isnumeric())
print(Example_Variable.isalpha())
print(Example_Variable.index("B"))
print(Example_Variable.isnumeric())
print(Example_Variable[3])
print("This is Mr. "+Example_Variable)
print(f"This is Mr. {Example_Variable}") 
print("This is Mr. {0}".format(Example_Variable))