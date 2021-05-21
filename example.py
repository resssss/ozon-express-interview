names = ['Ivan', 'Anton', 'Olga']
numbers = [1, 2, 3]

persons = dict()
for num, name in zip(numbers, names):
    persons[num] = name

print(persons)

n_names = list()

for k, v in persons.items():
    if len(v) > 4:
        print(v)
    if 'n' in v:
        n_names.append(v)

uniq_n_names = list()
for name in n_names:
    if name not in uniq_n_names:
        uniq_n_names.append(name)

print(uniq_n_names)

o_names = list(filter(lambda x: 'o' in x or 'O' in x, names))
print(o_names)
