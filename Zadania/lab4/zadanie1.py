# a
names = ["Anna", "Krzysztof", "Michał", "Paweł"]
print(sorted(names))
# b
names.extend(["Julia", "Tomasz"])
pop_name = names.pop()
print(pop_name)
# c
names.insert(2, "Adam")
print(names)
# d
names.reverse()
duplicated_names = names * 2
print(duplicated_names)
