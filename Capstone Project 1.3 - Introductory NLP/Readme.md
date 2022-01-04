# Capstone Project 1.3 - Introductory NLP and NLP Movie Suggestion
One of the Natural Language Processing projects I had to do

### Introduction to NLP
A written piece on how Natural Language Processing is used in [Grammarly](https://grammarly.com)

## Project Overview
This program reads in a list of movies on separate lines from an external text file, runs similarity analysis based on the description of the movies, and recommends to the user which 3 movies they should watch.

The program has two classes

- AllMovies - which reads in the movies
            - adds the movies to a dictionary based on a numerical key
            
- Recommendation - inherits from AllMovies class
                 - runs similarity analysis
                 - sorts the results in ascending order (Highest value = most recommended)
                 - Builds the recommendation list
                 - Displays the results to the user

- **Achievements:**
  - built a Movie Recommendation Program

- **What I learnt:**
  - How to utilize Natural Language Processing using SpaCy library
  - Tokenize and Lemitize words allowing them to be used mathematically
  - How to statistically measure a sentence and use it
