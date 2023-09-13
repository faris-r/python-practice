"""
Basic syntax demo
"""
# Sequential

print('Mom said, "Go to the shop"')
print('Budi said, "Okay what should i do there?"')
print('Mom said, "Buy 1 bottle of milk and if they had eggs, buy 6"')
print('Then Budi go to the store')

# Branch
milk_bottle_count = 4
egg_count = 6
print(f"There are {milk_bottle_count} bottles")
print(f"There are {egg_count} eggs")

if milk_bottle_count > 0:
    print("Budi checks the price, and his money is enough")
    print("Budi buys 1 milk bottle")
else:
    print("Budi doesnt buy milk")
if egg_count < 6:
    print(f"Budi buys {egg_count} egg(s)")
else:
    print("Budi buys 6 eggs")

print("Budi goes home")
print("Budi gives the result to his mom")
