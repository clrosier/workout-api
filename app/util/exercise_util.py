def exercises_with_categories(ex_cat):
    exercise_categories = {}
    for item in ex_cat:
        if item['cat_name'] not in exercise_categories:
            exercise_categories[item['cat_name']] = []
    
    for key, value in exercise_categories.items():
        for item in ex_cat:
            if item['cat_name'] == key:
                value.append(item['ex_name'])
    
    return exercise_categories
