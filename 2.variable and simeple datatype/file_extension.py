file_name = "https://python_note.txt"
message = file_name.removeprefix("https://").removesuffix(".txt")

print(message)
