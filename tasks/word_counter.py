# or use Counter('str').most_common(num)
def word_counter(file):
    words = []
    word_map = {}

    with open(file) as f:
        words.extend(f.readline().split())

    for word in words:
        if word not in word_map:
            word_map[word] = 1
        else:
            word_map[word] += 1
    return word_map
