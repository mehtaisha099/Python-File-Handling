strings = ["Python", "Java", "PHP", "C++", "C#"]

file = open("sentences.txt", "a")

for item in strings:
    file.write(item + "\n")

file.close()

print("Strings appended successfully.")