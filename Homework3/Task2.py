import re
from collections import Counter


def top_10_words(our_str: str):
    """В большой текстовой строке подсчитать количество встречаемых слов и вернуть 10 самых частых. Не учитывать знаки
    препинания и регистр символов. За основу возьмите любую статью из википедии или из документации к языку.
    """
    all_words = re.findall(r'\w+', our_str.lower())
    return Counter(all_words).most_common(10)