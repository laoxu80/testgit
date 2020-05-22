
def return_list(val, list=[]):
    print(list)
    list.append(val)
    return list


print(return_list(1))
print(return_list(2, []))
print(return_list(3))