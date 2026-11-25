source = open("sample.txt", "r")

content = source.read()

source.close()

backup = open("backup.txt", "w")

backup.write(content)

backup.close()

print("File backup created successfully.")