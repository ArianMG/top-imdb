import os
from imdb.imdb import IMDb

def main():
    train_dir = '/app/aclImdb/train/'
    imdb = IMDb(train_dir)
    
    imdb.process_reviews()
    best_movies = imdb.get_best_movies()
    worst_movies = imdb.get_worst_movies()

    print("Top 10 best rated movies on average:")
    for movie_id, avg_rating in best_movies:
        print(f"Movie ID: {movie_id}, Average Rating: {avg_rating:.2f}")

    print("Top 10 worst rated movies on average:")
    for movie_id, avg_rating in worst_movies:
        print(f"Movie ID: {movie_id}, Average Rating: {avg_rating:.2f}")

if __name__ == "__main__":
    main()