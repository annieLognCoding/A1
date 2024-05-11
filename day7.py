def reverse_each_word(sentence):
    words = sentence.split()
    reversed_words = [word[::-1] for word in words]
    return ' '.join(reversed_words)

def first_half(text):
    half_index = len(text) // 2
    if len(text) % 2 != 0:
        half_index += 1
    return text[:half_index]

def substrings_between(s, start, end):
    results = []
    parts = s.split(start)[1:]  # Skip the first split as it will not start with start
    for part in parts:
        if end in part:
            results.append(start + part.split(end)[0] + end)
    return results

def contains_xyz(s):
    count = 0
    i = 0
    while i < len(s) - 2:
        if s[i:i+3] == 'xyz':
            if i == 0 or s[i-1] != '.':
                count += 1
        i += 1
    return count
