#List Alternator Andrew Hayes 1/21/2025


# Function to alternate the elements of the two lists
def countList(list1, list2):
    return [sub[item] for item in range(len(list2))
                      for sub in [list1, list2]]
     
# alternate the elements of the two lists
list1 = [1, 2, 3]
list2 = [40, 50, 60]
print(countList(list1, list2))