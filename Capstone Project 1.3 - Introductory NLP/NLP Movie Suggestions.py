# -*- coding: utf-8 -*-
"""
Created on Fri Sep 10 19:46:56 2021

Dear Mentor

This program reads in a list of movies on separate lines from an external text file,
runs similarity analysis based on the description of the movies, and recommends
to the user which 3 movies they should watch.

The program has two classes

- AllMovies - which reads in the movies
            - adds the movies to a dictionary based on a numerical key
            
- Recommendation - inherits from AllMovies class
                 - runs similarity analysis
                 - sorts the results in ascending order (Highest value = most recommended)
                 - Builds the recommendation list
                 - Displays the results to the user

References: 
    https://stackabuse.com/how-to-sort-dictionary-by-value-in-python/
    https://stackoverflow.com/questions/16125229/last-key-in-python-dictionary

@author: Raman Sewjugath
"""



# Import spacy module
import spacy

# specify model to use
nlp = spacy.load('en_core_web_md')





#=====================================
#   ALL MOVIES CLASS
#=====================================
class AllMovies:
    
    '''
    Add movies from the external data source to a numerically ordered dictionary
    '''
    # initialize the constructor
    def __init__(self, external_data):
        self.external_data = external_data
        self.all_available_movies = ""
        self.movies_dict = {}
    
    # Function to add all movies from each line in a list
    def add_movies(self):
        # Create the key
        num = 1
        
        for movie in self.external_data:
            
            # stripped away the new line characters
            movie = movie.strip("\n").replace("\'", "")                   
            
            # add movie to list
            self.movies_dict[num] = movie
            
            num += 1    
    
    
    

#=====================================
#   MOVIE RECOMMENDATION CLASS
#=====================================

class Recommendation(AllMovies):
    
    '''
    Class to obtain the next movie a user should watch
    '''
    # initialize the constructor
    def __init__(self, watched_movie, external_data):
        super().__init__(external_data)
        self.watched_movie = watched_movie
        self.movie_tokens = {}
        self.sorted_tokens = {}
        
        # adds the movies using method from the parent class
        self.add_movies() 
        
    
    '''
    SIMILARITY ANALYSIS
    This method compares the users watched movie with each movie from the
    movies_dict and assigns a similarity value which is stored in a separate
    movie_tokens dictionary based on the same key (So we can later reference
    them in both dictionaries)
    '''
    def similarity(self):        
        movie_user_watched = nlp(self.watched_movie)
        key = 1
                
        for movie_to_watch in self.movies_dict:
            movie_to_watch = nlp(self.movies_dict[movie_to_watch])
            
            self.movie_tokens[key] = movie_user_watched.similarity(movie_to_watch)
            key += 1
        
    
    '''
    This method uses a new dictionary to add items of movie_tokens dictionary
    in ascending order based on the values
    REF: https://stackabuse.com/how-to-sort-dictionary-by-value-in-python/
    The above URL referenced a code which can order items in a dictionary
    based on the values.
    
    for each item in dict1, a reference key is used to reference the ordered
    items in the ordered list and add them to a new dictionary based on
    comparing their keys. if the current key in the loop is equal to a key in
    the list, then they are added to the new dictionary.
    '''        
    def sorting(self):
        
        #Sort the values out in ascending order in the movie tokens list        
        ordered_list = sorted(self.movie_tokens.values())
                
        for item_a in ordered_list:
            for item_b in self.movie_tokens.keys():
                if self.movie_tokens[item_b] == item_a:
                    self.sorted_tokens[item_b] = self.movie_tokens[item_b]
        
        
        

    '''
    This method finds the movies with the highest similarity values
    and prepares the top 3 for display to the user
    
    The below URL I used to find out how to index a dictionary, since a dictionary
    is not an ordered list.
    https://stackoverflow.com/questions/16125229/last-key-in-python-dictionary
    '''
    def we_recommend(self):
        
        # hold the recommended movies
        movies = ""
        
        # count how many movies to recommend
        count = 3
        
        # used to obtain movies starting from the end of the dictionary
        # since it ward orderd in ascending order
        num = -1
        
        while count != 0:
            movie_search = list(self.sorted_tokens)[num]
            result = movie_search
            
            # loop which concatenates the specified movies to a variable movies
            for movie in self.movies_dict:
                if movie == result:
                    
                    # each movie is split and the first two indeces are used
                    # since they contain the movie name
                    title = self.movies_dict[movie].split()                   
                    
                    # movie names are concatenated in movies variable
                    movies += title[0] + " " + title[1] + "\n\n"        
            
            count -= 1
            num -= 1        
        return movies
    
    
    # This method calls the similarity and sorting functions
    # then string method to format the output for the user
    def what_to_watch_next(self):
        self.similarity()
        self.sorting()
        return self.__str__()    
    
    # string method to format output for user
    def __str__(self):        
        movies = self.we_recommend()        
        return print(f"We Recommend the Following Movies:\n\n{movies}")
        
        
        
        


#==============================================================================
#      ARGUMENTS BELOW HERE
#==============================================================================

print("what to watch next?")

# open the list of movies from external data source
f = open('movies.txt', 'r')

# the movie the user has watched
movie_watched = "Planet Hulk :Will he save their world or destroy it? When the Hulk becomes too dangerous for the Earth, the Illuminati trick Hulk into a shuttle and launch him into space to a planet where the Hulk can live in peace. Unfortunately, Hulk land on the planet Sakaar where he is sold into slavery and trained as a gladiator."

# create the list of movies object to hold all the movies
mov = Recommendation(movie_watched, f)

# calling functions to get similarity and dsiplay to user
mov.what_to_watch_next()
    
f.close()

