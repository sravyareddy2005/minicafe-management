menu = {
    'pizza':50,
    'burger': 100,
    'chicken':200,
    'biryani':300,
    'mutton biryani':450
}
total = 0
while True:
    item = input("Enter item: ")
    if item in menu:
        total = total + menu[item]
        print(item, "added")
    else:
        print("Item not available")
    more = input("Anything else? yes/no: ")
    if more == "no":
        break
print("Total bill =", total)