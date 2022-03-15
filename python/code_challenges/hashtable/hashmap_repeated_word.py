from heapq import heappop, heappush
import re


def find_repeated_word(text):
    freq_map = dict()
    for word in text.split(" "):
        word = word.lower()
        word = re.sub('[^a-zA-Z0-9]', '', word)
        print(word)
        if word in freq_map:
            return word
        
        freq_map[word] = 1


def find_top_k_repeated_words(text, k):
    freq_map = dict()
    heap = []
    for word in text.split(" "):
        word = word.lower()
        word = re.sub('[^a-zA-Z0-9]', '', word)
        if word in freq_map:
            freq_map[word] = freq_map.get(word) + 1
        else:
            freq_map[word] = 1

    for word, freq in freq_map.items():
        if len(heap) < k:
            heappush(heap, (freq, word))
        else:
            if freq > heap[0][0]:
                heappop(heap)
                heappush(heap, (freq, word))
    res = []
    for pair in heap:
        res.append(pair[1])
    return res

    
