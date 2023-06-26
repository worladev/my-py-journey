menu = ["espresso", "mocha", "latte", "cappuccino", "cortado", "americano"]

def find_coffee(coffee):
    if coffee[0] == 'c':
        return coffee

#Using map()
map_coffee = map(find_coffee, menu)
# returns a map object
print(map_coffee)
for x in map_coffee:
    print(x)


#Using filter()
filter_coffee = filter(find_coffee, menu)
# returns a filter object
print(filter_coffee)
for x in filter_coffee:
    print(x)