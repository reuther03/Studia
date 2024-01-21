import keyword

slowa = ["for", "print", "break", "done", "bad"]

for slowo in slowa:
    print(slowo, keyword.iskeyword(slowo))

