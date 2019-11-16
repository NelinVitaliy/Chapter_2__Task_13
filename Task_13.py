x = int(input("Give me a number: "))
print("All the squares in the given range: ")
print([i**2 for i in range(1, x+1) if i**2 <= x])
