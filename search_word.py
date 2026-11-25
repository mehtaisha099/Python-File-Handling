word = input("Enter a word to search: ")

file = open("sample.txt", "r")

for line in file:
    if word.lower() in line.lower():
        print(line.strip())

file.close()