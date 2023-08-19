def combinations():
    friends = {
            'Andrew': ('keys', 'tent', 'net', 'food'),
            'Matthew': ('sleeping bag', 'net', 'toilet paper', 'food'),
            'Jack': ('water', 'food', 'clothers', 'insect spray')
          }

    res = set(friends['Andrew']) & set(friends['Matthew']) & set(friends['Jack'])

    print('взяли все три друга: ')
    print(res)
    res.clear()

    res = (set(friends['Andrew']) - set(friends['Matthew']) - set(friends['Jack'])).union(
          (set(friends['Matthew']) - set(friends['Andrew']) - set(friends['Jack'])).union(
          (set(friends['Jack']) - set(friends['Andrew']) - set(friends['Matthew']))))

    print('вещи уникальны, есть только у одного друга: ')
    print(res)

    our_dict = {}

    our_dict[str((set(friends['Andrew']) | set(friends['Matthew'])).difference(set(friends['Jack'])))] = 'Jack'
    our_dict[str((set(friends['Jack']) | set(friends['Matthew'])).difference(set(friends['Andrew'])))] = 'Andrew'
    our_dict[str((set(friends['Jack']) | set(friends['Jack'])).difference(set(friends['Andrew'])))] = 'Matthew'

    print('есть у всех друзей кроме одного и имя того, у кого данная вещь отсутствует: ')
    for key, value in our_dict.items():
        print(f'У {value} нет {key}')