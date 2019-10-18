''' # Lab 11: Wall Painting
We're re-painting one wall of a room; let's figure out how much it's going to cost.
Assume one gallon of paint covers 400 square feet.

## Ask the user for:
1. width of the wall
2. height of the wall
3. how much a gallon of paint costs
Figure out then print how much it will cost to paint the wall with one coat.

## Advanced
- Also ask the user for how many coats they're going to put on, then calculate the cost of paint.
- Problem: you can only buy whole gallon cans of paint. Figure out a way to round up your wall calculation so you know how many whole gallons cans to buy.
- Allow the user to enter multiple walls' dimensions-- add the total areas together before calculating the cost.
'''
print('''
Hello, this script calculates wall area and how much it costs to paint that wall.
If you provide the wall size and paint cost, we'll do the math. 🤖✌️
'''
)
# beginning to build a standard error catching func
# def input_must_be_int(input):
#     try:
#         print(input / 1)
#         print("Thanks for good input")
#     except:
#         print("Please enter only numbers when using this script. Try again? (↑ , ⏎ )")

width = int(input("What is the width of the wall (just give a number)?  "))
height = int(input("What is the height of the wall (just give a number)?  "))
per_gal = float(input("How much for a gallon of that hipster paint you insist on using? Decimals are fine. "))

how_much_paint = (width * height)/400 # 1 gallon coats 400 sqft
so_this_will_cost = how_much_paint * per_gal

print(f"Radical! You can give that wall 1 coat of paint using:\n🎨 {how_much_paint} gallons of paint\nSo paint for this project will cost:\n💸 ${so_this_will_cost}\nWay to be a DIYer, brah!")
