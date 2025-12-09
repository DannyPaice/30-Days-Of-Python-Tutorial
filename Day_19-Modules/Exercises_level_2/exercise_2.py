

def find_most_common_words(file, num):
    with open(file, "r") as f:
        file = f.readlines()
    
    word_dict = {}
    for line in file:
        words = line.strip().split()
        for w in words:
            if w not in word_dict:
                word_dict[w] = 1
            else:
                word_dict[w] += 1
    
    sorted_items = sorted(word_dict.items(), key=lambda x: x[1], reverse=True)
    return sorted_items[:num]

print(find_most_common_words('Day_19-Modules/Exercises_level_2/obama_speech.txt', 10))


