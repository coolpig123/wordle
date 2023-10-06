def analyze_colors(word, correct_word):
    t_word = word.copy()
    t_correct_word = correct_word.copy()

    for i in range(0, 5):
        if t_word[i] == t_correct_word[i]:
            t_word[i] = 'g'
            t_correct_word[i] = 'g'

    for i in range(0, 5):
        if t_word[i] in t_correct_word and t_word[i] != 'g':
            t_correct_word[t_correct_word.index(t_word[i])] = 'y'
            t_word[i] = 'y'

    for i in range(0, 5):
        if t_word[i] != 'g' and t_word[i] != 'y':
            t_word[i] = 'b'

    return t_word