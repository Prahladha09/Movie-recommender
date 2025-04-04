import numpy as np
import pandas as pd
def Recommended_movies(data, way, rating=5, Genre=[], number_of_movies=5):
    data = data.copy()
    data['Genre'] = data['Genre'].astype(str).apply(lambda x: [g.strip().lower() for g in x.split(',')])

    if way == 1:
        data['diff'] = abs(data['Rating'] - rating)
        nearest_movies = data.sort_values(by='diff')
        return nearest_movies[['Movie', 'Genre', 'Rating']].head(min(len(nearest_movies), number_of_movies))
    
    elif way == 2:
        Genre = [g.strip().lower() for g in Genre]
        data_filtered = data[data['Genre'].apply(lambda x: all(genre in x for genre in Genre))].copy()
        data_filtered['diff'] = abs(data_filtered['Rating'] - rating)
        nearest_movies = data_filtered.sort_values(by='diff')
        return nearest_movies[['Movie', 'Genre', 'Rating']].head(min(len(nearest_movies), number_of_movies))
