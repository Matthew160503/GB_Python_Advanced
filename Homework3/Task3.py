import itertools

MAX_LIMIT = 250

def max_weight_for_hike():
    hike_things = {
        "зажигалка": 5,
        "одежда": 50,
        "нож": 25,
        "палатка": 37,
        "еда": 10,
        "вода": 18,
        "спрей от насекомых": 5,
        "удочка": 35,
        "мангал": 24,
        "стулья": 29,
        "приборы": 13,
        "очки": 7,
    }

    for i in itertools.permutations(hike_things.values(), MAX_LIMIT):
        print(i)
    return None