# LEEME.md

## Analysis of the Best and Worst IMDb Movies

This project performs an analysis of the top 10 best and worst movies from the IMDb database using two approaches: UNIX-style command-line tools and a modular Python solution. Below are the instructions for running both approaches inside a Docker container.

## Requirements
* docker: "^27.3.1"
* docker compose: "^2.26.1"

## Instructions to Run the Project
### 1. Clone the Repository
``` bash
    https://github.com/ArianMG/top-imdb
    cd top-films
```
### 2. Build the Containers

Before running the analysis, you need to build the Docker container.
``` bash
    docker compose build
```
### 3. Start the Containers

Once the containers are built, start the environment in detached mode (running in the background):
``` bash
    docker compose up -d
```
## Analysis with Python

To perform the analysis using Python, you can run the following command inside the container:

``` bash
    docker exec top-imdb-container python python/scripts/top_movies.py
```

This command runs the analysis to find the top 10 best and worst movies using a modular Python script. The results will be displayed in the terminal.

## Analysis with Command-Line Tools

To perform the analysis using UNIX command-line tools, first ensure the script has execution permissions:
``` bash
    docker exec top-imdb-container chmod +x cmd/top_movies.sh
```

Then, run the script:
``` bash
    docker exec top-imdb-container bash cmd/top_movies.sh
```

## Project Directories

* **aclImdb/** Contains the IMDB database for analysis. The files should be in this directory

* **cmd/**: Contains the files related to solving the problem using command-line tools (UNIX philosophy).
    
* **python/**: Contains the files related to solving the problem using Python. This includes a module named *imdb* and scripts for running the analysis.
    * **scripts/**: Auxiliary Python scripts.
    * **notebooks/**: Jupyter notebooks for interacting with the analysis.