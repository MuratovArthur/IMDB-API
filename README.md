# IMDB API App

## Task

The task was to create a backend API that would enable users to look for movies based on genre.

## Description

This Python project is a Flask web application that allows users to search for movies based on their genres. The application loads movie data from a CSV file called imdb-movie-data.csv and provides several endpoints for searching movies by different genres like Action, Adventure, Comedy, Drama, and Romance.

## Requirements

1. Python 3.6 or higher
2. Flask


## Installation
Clone the repository or download the source code.

## Running the Application
Run the Flask application:
```
python app.py
```
The application will be available at http://0.0.0.0:8080/.

## Usage
You can search for movies in different genres using the following endpoints:

`/action`: List all Action movies.

`/adventure`: List all Adventure movies.

`/comedy`: List all Comedy movies.

`/drama`: List all Drama movies.

`/romance`: List all Romance movies.

To search for movies in a specific genre, use the following endpoint:
/?genre=<genre>: Replace <genre> with the genre you want to search for. For example, `/?genre=Sci-Fi` will return all Sci-Fi movies.
The search is case-insensitive, so you can use "sci-fi" or "Sci-Fi". The response will be a JSON object containing the matching movies' details.
```
python app.py
curl "http://localhost:8080?genre=action"
```
