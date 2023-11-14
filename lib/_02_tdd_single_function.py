def make_snippet(string):
    words = string.split()[:5]
    if len(string.split()) > len(words):
        words.append("...")
        return " ".join(words)
    return string
    

def count_words(string):
    words = string.split()
    return len(words)
