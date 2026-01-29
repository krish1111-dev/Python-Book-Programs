Guest_list = ["Himanshu bhai ", "Pravin bhai", "Dishant bhai"]

# replace name
print(f"sorry, {Guest_list[2]} can't make it to the dinner")
Guest_list[2] = 'Meet'


# insert name
Guest_list.insert(0, 'Jay bhai')
Guest_list.insert(2, "Krish bhai")
Guest_list.append("Rajveer bhai")

print("\n You can arrive only two people for dinner")

# remove name using pop method
remove_guest = Guest_list.pop()
print(f"you're {remove_guest} sorry you can't invite them to dinner")
remove_guest = Guest_list.pop()
print(f"you're {remove_guest} sorry you can't invite them to dinner")
remove_guest = Guest_list.pop()
print(f"you're {remove_guest} sorry you can't invite them to dinner")
remove_guest = Guest_list.pop()
print(f"you're {remove_guest} sorry you can't invite them to dinner")


# print name for dinner
print("\n final invitation")
print(f"{Guest_list[0]}, You are still invited for dinner")
print(f"{Guest_list[1]}, You are still invited for dinner")


# deleter name
del Guest_list[1]
del Guest_list[0]

print("Guest list after dinner")
print(Guest_list)
