'''
### CHECK AGAIN
Return for set does not allow duplicate values.

'''
print("\n")

set_num = {1, 3, 1, 14, 44, 9}
print(set_num)

# set evaluates True as 1 and False as 0
new_set = {"coding", "CWD", 1, 2, 3, False, True, 0}
print(new_set)

'''Set Methods'''
# .add()
set_num.add(2)
print(set_num)

add_set = set()
for i in range(0, 6):
    add_set.add(i)

print(add_set)

# .union()
people = {"Jay", "Idrisu", "Archil"}
vampires = {"Karen", "Arjun"}
dracula = {"Deepanshu", "Raju"}

new_set_union = people.union(vampires)
print(new_set_union)

new_set_union2 = vampires.union(dracula)
print(new_set_union2)

#using the pipe (|)
new_set_union2 = vampires|dracula
print(new_set_union2)


# .intersection()
new_set_inter1 = set()
new_set_inter2 = set()

for i in range(1, 6):
    new_set_inter1.add(i)

for i in range(3, 9):
    new_set_inter2.add(i)

inter_set = new_set_inter1.intersection(new_set_inter2)
print(inter_set)


#using & for intersection.
inter_set = new_set_inter1 & new_set_inter2
print(inter_set)


# .difference()
print(new_set_inter1)
print(new_set_inter2)

inter_set = new_set_inter1.difference(new_set_inter2)
print(inter_set)

# .clear()


# More soon