a = input().split()
new = ""

for word in a:
    new += word[0]
    for i in range(1, len(word)):
        if word[i] != word[i - 1]:
            new += word[i]
    new += " "  # Add space after each word

print(new.strip())
