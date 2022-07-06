def age_assignment(*names, **kwargs):
    assigmennt = {}
    for name in names:
        for letter, age in kwargs.items():
            if name.startswith(letter):
                assigmennt[name] = age
    return assigmennt


print(age_assignment("Peter", "George", G=26, P=19))

# {'Peter': 19, 'George': 26}
