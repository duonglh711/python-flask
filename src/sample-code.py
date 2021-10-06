#string format
var1 = "Test1"
var2 = "Test2"
ex1 = f"{var1} {var2} ..."
ex2 = "{} {}".format(var1, var2)

#user input
size_input = input("How pig is your house (in square feet): ")
square_feet = int(size_input)
square_metres = square_feet/10.8
print(f"...{square_feet} ... {square_metres:.2f}")

#lists, tuples, sets
list = ["a", "b", "c"]
