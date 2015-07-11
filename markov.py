import sys
import random 
input_files = sys.argv[1:]


#renaming this temporarily from SimpleMarkovGenerator to SimpleMG
#because it's long to type
class SimpleMG(object):


    def __init__(self, filenames):
        self.words = self.read_files(filenames)
        self.dictionary = self.make_chains()


    def read_files(self, filenames):
        """Given a list of files, make chains from them."""
        self.filenames = filenames 
        words = []
        for the_file in self.filenames: 
            file_contents = open(the_file).read()
            words += file_contents.split()
        return words


        # self.words = []
        # final_string = []
        # self.filenames = filenames
        # for file in filenames:
        #     words = open(filenames) 
        #     words = file.split()
        #     final_string += words
        # print final_string

    def make_chains(self):
        """Takes input text as string; stores chains."""

        self.chains = {}
        for i in range(len(self.words) - 2):
            key = (self.words[i], self.words[i + 1])
            value = self.words[i + 2]

            if key not in self.chains:
                self.chains[key] = []

            self.chains[key].append(value)

    

        # or we could say "chains.setdefault(key, []).append(value)"
        return self.chains
    def make_text(self):
        """Takes dictionary of markov chains; returns random text."""
        key = random.choice(self.chains.keys())
        words = [key[0], key[1]]
        character_count = 0
        while key in self.chains and character_count < 130:
            # Keep looping until we have a key that isn't in the chains
            # (which would mean it was the end of our original text)
            #
            # Note that for long texts (like a full book), this might mean
            # it would run for a very long time.

            word = random.choice(self.chains[key])
            words.append(word)
            key = (key[1], word)
            character_count += len(word)

        return " ".join(words)
            


if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    generator = SimpleMG(input_files)
    print generator.make_text()
    # we should call the read_files method with the list of filenames
    # we should call the make_text method 5x


    


