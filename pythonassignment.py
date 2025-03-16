#  creating an empty list called "my_list"
my_list = []

# appendind(putting) 10,20,30,40 to my_list
my_list.append(10)
my_list.append(20)
my_list.append(30)
my_list.append(40)

# inserting(adding) 1,15 to my_list
my_list.insert(1,15) 

# created another list called "your_list"
your_list = [50,60,70]

# extended(joining) your_list to my_list
my_list.extend(your_list)

# removed 70 from my_list
my_list.remove(70)

# arranged my_list it in ascending order
my_list.sort()

# found and printed the index value of 30 in my_list
print(my_list[3])
