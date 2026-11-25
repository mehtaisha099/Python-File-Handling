file = open("sentences.txt", "w")

for i in range(5):
    sentence = input("Enter sentence " + str(i + 1) + ": ")
    file.write(sentence + "\n")

file.close()

print("5 sentences saved successfully.")