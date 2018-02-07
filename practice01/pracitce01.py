L = ['Michael', 'Sarah', 'Tracy', 'Bob', 'Jack']

# new_list =  [L[0], L[1], L[2]]



new_list= []
for i in range(3):
    new_list.append(L[i])
new_list2 = L[2:5]

print(new_list)

print(new_list2)

list_3 = [(1,2),(3,4),(7,4)]

def point_in_list(point_new,point_list):
    for point in point_list:
        if point_new[0]== point[0] and point_new[1] == point[1]:
            return True

new_list3 = []

for x in range(10):
    for y in range(10):
        if not point_in_list((x,y),list_3):
            new_list3.append((x,y))
# print(new_list3)

new_list4 = [(x,y) for x in range(10) for y in range(10) if not point_in_list((x,y),list_3)]
print(new_list4)