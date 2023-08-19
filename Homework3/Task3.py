from itertools import permutations

MAX_LIMIT = 100


def max_weight_for_hike():
    hike_things = {
        "зажигалка": 5,
        "одежда": 50,
        "нож": 25,
        "палатка": 37,
        "еда": 10,
        "вода": 18,
        "удочка": 35,
        "мангал": 24,
        "стулья": 29,
        "приборы": 13,
    }

    all_choise = permutations(hike_things.items())
    result_dict = {}
    for temp_set in all_choise:
        temp_available_weight = MAX_LIMIT
        possible_variant_set = set()
        for thing, weight in temp_set:
            if temp_available_weight >= weight:
                temp_available_weight -= weight
                possible_variant_set.add(thing)
        result_dict[tuple(possible_variant_set)] = MAX_LIMIT-temp_available_weight

    print("Все доступные варианты: ")
    for thing, weight in result_dict.items():
        print(f'Вещи = {thing} занимают {weight} места в рюкзаке')