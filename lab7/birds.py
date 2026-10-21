# Jack Trieu
# Prof. Pulatov
# CSC 231, section 002
# 4/2/2026
import time
from hashmap import HashMap
def read_birds_hashmap(filename):
   """
   :param filename: the name of the file to open.
   :return: the HashMap containing the count of bird species
   """
   birds = HashMap(1000000)
   with open(filename, 'r') as file:
      for b in file:
         if not b in birds:
            birds[b] = 1
         else:
            birds[b] +=1
            
      
      


def read_birds_dictionary(filename):
   """
   :param filename: the name of the file to open.
   :return: the dictionary containing the count of bird species
   """
   birds = {}
   with open(filename, 'r') as file:
      for b in birds:
         if not b in birds:
            birds[b] = 1
         else:
            birds[b] +=1



if __name__ == "__main__":
   # You can add lines of code here to help you test.

   # ---- DO NOT MODIFY THE LINES BELOW ----
   start = time.perf_counter()
   print('-' * 3, "Reading bird_observations_small.txt with Python dictionary", '-' * 3)
   results = read_birds_dictionary("bird_observations_small.txt")

   print('\n', '-' * 3, "Reading bird_observations_large.txt with Python dictionary", '-' * 3)
   results = read_birds_dictionary("bird_observations_large.txt")
   read_time = time.perf_counter() - start
   print('-' * 3, "Total time for reading bird_observations_large.txt with Python dictionary = ", read_time, '-' * 3, '\n')


   start = time.perf_counter()
   print('-' * 3, "Reading bird_observations_small.txt with my HashMap implementation", '-' * 3)
   results = read_birds_hashmap("bird_observations_small.txt")

   print('\n', '-' * 3, "Reading bird_observations_large.txt with my HashMap implementation", '-' * 3)
   results = read_birds_hashmap("bird_observations_large.txt")
   read_time = time.perf_counter() - start
   print('-' * 3, "Total time for reading bird_observations_large.txt with my HashMap implementation = ", read_time, '-' * 3, '\n')
