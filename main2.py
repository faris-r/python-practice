"""
Basic syntax demo
"""
# Sequential

print('Mom said, "Go to the shop"')
print('Budi said, "Okay what should i do there?"')
print('Mom said, "Buy 1 bottle of milk and if they had eggs, buy 6"')
print('Then Budi go to the store')

# Branch
milk_bottle_count = 20
egg_count = 0
print(f"There are {milk_bottle_count} bottles")
print(f"There are {egg_count} eggs")

if milk_bottle_count > 0:
    print("Budi checks the price, and his money is enough")
    if egg_count == 0:
        print("Budi buys 1 milk bottle")
    else:
        print("Budi buys 6 milk bottles")
else:
    print("Budi doesn't buy 1 milk bottle")
print("Budi goes home")
print("Budi gives the result to his mom")
