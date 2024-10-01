#!/bin/bash

# Define base directory
train_dir="aclImdb/train/"

# Temporary file to store ids and ratings
ratings_file="movie_ratings.txt"
avg_file="movie_avg_ratings.txt"
sorted_file="sorted_movies.txt"

# Clean previous files if they exist
rm -f $ratings_file $avg_file $sorted_file

# Extract ids and ratings from files in pos/ and neg/
echo "Extracting IDs and ratings from reviews..."
ls ${train_dir}pos/*.txt ${train_dir}neg/*.txt | sed 's/.*\///' | sed 's/\.txt//' | awk -F'_' '{print $1, $2}' > $ratings_file

# Calculate the average rating per movie
echo "Calculating the average rating per movie..."
awk '{ratings[$1]+=$2; count[$1]++} END {for (id in ratings) print id, ratings[id]/count[id]}' $ratings_file > $avg_file

# Sort movies by average rating
echo "Sorting movies by average rating..."
sort -k2 -n $avg_file > $sorted_file

# Show the 10 worst rated movies
echo "The 10 worst rated movies are:"
head -n 10 $sorted_file

# Show top 10 rated movies
echo "The top 10 rated movies are:"
tail -n 10 $sorted_file

echo "Process completed."

