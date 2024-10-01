import os
import re
from collections import defaultdict

class IMDb:
    def __init__(self, train_dir):
        self.train_dir = train_dir
        self.movie_ratings = defaultdict(list)

    def process_reviews(self):
        for sentiment in ['pos', 'neg']:
            sentiment_dir = os.path.join(self.train_dir, sentiment)
            for filename in os.listdir(sentiment_dir):
                if filename.endswith('.txt'):
                    # Extract ID and rating from file name
                    match = re.match(r'(\d+)_(\d+)\.txt', filename)
                    if match:
                        movie_id = match.group(1)
                        rating = int(match.group(2))
                        # Add the rating to the corresponding movie list
                        self.movie_ratings[movie_id].append(rating)

    def calculate_avg_ratings(self):
        return {movie_id: sum(ratings) / len(ratings) for movie_id, ratings in self.movie_ratings.items()}

    def get_sorted_movies(self):
        movie_avg_ratings = self.calculate_avg_ratings()
        return sorted(movie_avg_ratings.items(), key=lambda x: (x[1], x[0]))

    def get_worst_movies(self, n=10):
        sorted_movies = self.get_sorted_movies()
        return sorted_movies[:n]

    def get_best_movies(self, n=10):
        sorted_movies = self.get_sorted_movies()
        return sorted_movies[-n:]

