my_list = []
my_list.extend([10, 20, 30, 40])  
my_list[2] = 15  
my_list.extend([50, 60, 70])
my_list.sort()
my_list.remove(70)
print(my_list)
