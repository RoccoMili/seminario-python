def line_count(text_list):
    return len(text_list)

def word_count(phrase):
    count = len(phrase.split())
    return count

def words_average(text_list):
    count = len(text_list)
    if (count == 0):
        return 0
    return sum(word_count(phrase) for phrase in text_list) / count
