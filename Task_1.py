def cook(cook_book: list, person: int):
    result = []
    # самостоятельно напишите код решения:
    for dish in cook_book:
        dish_name = dish[0]
        ingredients = dish[1]
        formatted_ingredients = []
        for ingredient in ingredients:
            name = ingredient[0]
            amount = ingredient[1] * person
            unit = ingredient[2]
            formatted_ingredients.append(f'{name} {amount} {unit}')
        result.append(f"{dish_name}: {', '.join(formatted_ingredients)}")
    return result


def fio(initials):
    f = initials[0][0]
    i = initials[1][0]
    o = initials[2][0]
    return f + i + o


def top_names(mentors):
    all_list = []
    for m in mentors:
        for name in m:
            all_list.append(name)

    all_names_list = []
    for mentor in all_list:
        name = mentor.split()
        all_names_list.append(name[0])
    unique_names = sorted(set(all_names_list))

    popular = []
    for name in unique_names:
        count = all_names_list.count(name)
        popular.append([name, count])
    popular.sort(key=lambda x: x[1], reverse=True)
    top_3 = popular[:3]
    result = "".join(
        f"{top_3[0][0]}: {top_3[0][1]} раз(а), {top_3[1][0]}: {top_3[1][1]} раз(а), {top_3[2][0]}: {top_3[2][1]} раз(а)")
    return result