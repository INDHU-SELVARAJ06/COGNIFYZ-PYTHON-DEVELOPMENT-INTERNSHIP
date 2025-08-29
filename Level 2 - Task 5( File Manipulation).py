def count_words(text):
    text = text.lower()
    words = text.split()
    unique =[]

    for w in words:
        w=w.strip(".,|?;:(){}[]\"'")
        if w!= "":
            unique.append(w)

    a= sorted(set(unique))
    for w in a:
        print(w,":", unique.count(w))

text = input("Enter Text : ")
count_words(text)
