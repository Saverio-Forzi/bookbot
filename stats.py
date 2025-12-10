def count_words (path):
    num_words = 0
    with open(path) as f:
        word_list = f.read()
        word_list = word_list.split()
        for w in word_list:
            num_words += 1
    return print(f"Found {num_words} total words")

def sort_on(items):
    return items["num"]

def count_characters (path):
    c_dict = {}
    with open(path) as f:
        text = f.read()
        for ch in text:
            if not ch.isalpha():
                continue
            ch = ch.lower()
            if not ch in c_dict:
                c_dict[ch] = 1
            else:
                c_dict[ch] += 1

    d_list = []
    for ch, count in c_dict.items():
        crop_dict = {"char": ch, "num": count}
        d_list.append(crop_dict)

    d_list.sort(reverse=True, key=sort_on)

    return d_list

