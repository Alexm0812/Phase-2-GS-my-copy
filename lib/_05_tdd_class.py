class DiaryEntry:
    def __init__(self, title, contents):
        self.title = title
        self.contents = contents
        self.words_read = 0

    def format(self):
        return f"{self.title}: {self.contents}"

    def count_words(self):
        # Returns:
        #   int: the number of words in the diary entry
        words = self.format().split()
        return len(words)

    def reading_time(self, wpm):
        if wpm == 0:
            raise Exception("Cannot be 0")

        # Parameters:
        #   wpm: an integer representing the number of words the user can read 
        #        per minute
        # Returns:
        #   int: an estimate of the reading time in minutes for the contents at
        #        the given wpm.
        word_count = self.contents.split()
        reading_time = len(word_count) / wpm
        return reading_time
    

    def reading_chunk(self, wpm, minutes):
        # Parameters
        #   wpm: an integer representing the number of words the user can read
        #        per minute
        #   minutes: an integer representing the number of minutes the user has
        #            to read
        # Returns:
        #   string: a chunk of the contents that the user could read in the
        #           given number of minutes
        #
        # If called again, `reading_chunk` should return the next chunk,
        # skipping what has already been read, until the contents is fully read.
        # The next call after that should restart from the beginning.
        test = minutes * wpm
        word_count = self.contents.split()
        if self.words_read > len(word_count):
            self.words_read = 0
        
        chunk_start = self.words_read
        chunk_end = self.words_read + test
        chunk = word_count[chunk_start:chunk_end]
        
        self.words_read = chunk_end
        
        return " ".join(chunk)
        




#2 (Challenge)
class GrammarStats():
    def __init__(self):
        self.counter_checked = 0
        self.counter_passed = 0

    def check(self, text):
        punc = ["!", "."]
        if text[0] == text[0].upper():
            for i in punc:
                if text[-1] == i:
                    self.counter_checked += 1
                    self.counter_passed += 1
                    return True
            self.counter_checked += 1
        else:
            return False





    def percetage_good(self):
        return int((self.counter_passed/ self.counter_checked) * 100)
