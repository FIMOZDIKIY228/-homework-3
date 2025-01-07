import random
friends = ["Анна", "Борис", "Виктор", "Галина", "Дмитрий"]
gifts = ["игрушка", "книга", "шарф", "носки", "конфеты", "часы", "фотоальбом"]
def choose_gifts(friends, gifts):
    random.shuffle(gifts)
    result = []
    for friends, gifts in zip(friends, gifts):
        result.append(f"{friends} получит {gifts}.")
    return ', '.join(result)
print(choose_gifts(friends, gifts))
