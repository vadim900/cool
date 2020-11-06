
infile = open('Я (Романтика).txt')
words = 0
char = 0
d = 0
for line in infile:
    wordslist = line.split()
    words = words + len(wordslist)
    char = char + len(line)
    d+=1
print("Кількість унікальних слів: %d" % int(d))
print("Слів в тексті: " + str(words))
print("Символів в тексті: " + str(char))
