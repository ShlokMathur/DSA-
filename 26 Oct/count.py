word = input()
count = 0
a = []
found = input()
for letter in word:
    if letter == found:
        count = count + 1
    else:
        count = 0
    a.append(count)
print(sum(a))
