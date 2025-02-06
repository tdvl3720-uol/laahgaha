def get_ordered_list(lst=None):
    if lst is None:
        user_input = input("Enter a list of integers, seprated by commas")
        lst = list(map(int,user_input.split(',')))
    return sorted(lst)

list = (1,0,2,3,4,5)
print(get_ordered_list(list))