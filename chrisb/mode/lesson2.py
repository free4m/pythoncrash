#!/usr/bin/python

import numpy

city_population = {
  'Tokyo': 13350000, # a key-value pair
  'Los Angeles': 18550000,
  'New York City': 8400000,
  'San Francisco': 1837442,
}

municipalities = {
    'New York City': [
        'Manhattan',
        'The Bronx',
        'Brooklyn',
        'Queens',
        'Staten Island'
    ],
    'Tokyo': [
        'Akihabara', 
        'Harajuku', 
        'Shimokitazawa', 
        'Nakameguro', 
        'Shibuya', 
        'Ebisu/Daikanyama', 
        'Shibuya District', 
        'Aoyama', 
        'Asakusa/Ueno', 
        'Bunkyo District', 
        'Ginza', 
        'Ikebukuro', 
        'Koto District', 
        'Meguro District', 
        'Minato District', 
        'Roppongi', 
        'Shinagawa District', 
        'Shinjuku', 
        'Shinjuku District', 
        'Sumida District', 
        'Tsukiji', 
        'Tsukishima']
}

population_values = city_population.values()
print numpy.mean(population_values)
