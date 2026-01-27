first = "john"
last = "wick"
full_name = f"{first} {last}!"

print(full_name)
print(f"Hello,{full_name.title()}")


message = f"Hello {full_name.title()}"
print(message)

print("Python")
print("\tPython")  # tab \t
print("languages:\n\tPython\nJavaScript\nC\nNode")


favorite_language = "      Python     "
print(favorite_language)
print(favorite_language.strip())  # remove space form both side
print(favorite_language.rstrip())  # remove space form right side
print(favorite_language.lstrip())  # remove space form left side


# removing prefixes
url = "https://instagram.com"
insta = url.removeprefix("https://")  # removeprefix
print(insta)

bike = "Hero Honda ZMR"
zmr = bike.removeprefix("Hero Honda")
print(zmr)
