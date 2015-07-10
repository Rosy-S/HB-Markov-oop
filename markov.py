import sys
import random 
input_files = sys.argv[1:]



class SimpleMarkovGenerator(object):


    def __init__(self, filenames):
        self.read_files(filenames)


    def read_files(self, filenames):
        """Given a list of files, make chains from them."""
        self.filenames = filenames 
        words = []
        for the_file in self.filenames: 
            file_contents = open(the_file).read()
            words += file_contents.split()
        print words


        # self.words = []
        # final_string = []
        # self.filenames = filenames
        # for file in filenames:
        #     words = open(filenames) 
        #     words = file.split()
        #     final_string += words
        # print final_string

    def make_chains(self, corpus):
        """Takes input text as string; stores chains."""
        pass

        # your code here

    def make_text(self):
        """Takes dictionary of markov chains; returns random text."""
        pass
        # your code here


if __name__ == "__main__":

    # we should get list of filenames from sys.argv
    # we should make an instance of the class
    # we should call the read_files method with the list of filenames
    # we should call the make_text method 5x

    pass
    


