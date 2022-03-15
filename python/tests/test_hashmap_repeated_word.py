from code_challenges.hashtable.hashmap_repeated_word import find_repeated_word, find_top_k_repeated_words


def test_find_repeated_words_text1():
    text = "Once upon a time, there was a brave princess who..."
    actual = find_repeated_word(text)
    expected = "a"
    assert actual == expected

def test_find_repeated_words_text2():
    text = "It was the best of times, it was the worst of times, it was the age of wisdom, it was the age of foolishness, it was the epoch of belief, it was the epoch of incredulity, it was the season of Light, it was the season of Darkness, it was the spring of hope, it was the winter of despair, we had everything before us, we had nothing before us, we were all going direct to Heaven, we were all going direct the other way – in short, the period was so far like the present period, that some of its noisiest authorities insisted on its being received, for good or for evil, in the superlative degree of comparison only..."
    actual = find_repeated_word(text)
    expected = "it"
    assert actual == expected

def test_find_repeated_words_text3():
    text = "It was a queer, sultry summer, the summer they electrocuted the Rosenbergs, and I didn’t know what I was doing in New York. why . I don't know why ."
    actual = find_repeated_word(text)
    expected = "summer"
    assert actual == expected

def test_find_top_k_repeated_words():
    text = "It was a queer, sultry summer, the summer, they electrocuted the Rosenbergs, and I I I I I didn’t know what I was doing in New York. why why . why don't I know why ."
    actual = find_top_k_repeated_words(text, 3)
    expected = ["was", "i", "why"]
    assert expected == actual

