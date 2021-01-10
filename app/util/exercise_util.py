def exercises_with_categories(excat):
    exercises = {}
    for item in excat:
        if item['ex_name'] not in exercises:
            exercises[item['ex_name']] = []
    
    for key, value in exercises.items():
        for item in excat:
            if item['ex_name'] == key:
                value.append(item['cat_name'])
    
    return exercises
