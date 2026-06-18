# Movie-recommendations-system1
Personalized Movie Recommendation System

Overview

This project is a simple movie recommendation system developed in Python using the K-Nearest Neighbor (KNN) approach. The system recommends movies to users based on their ratings and similarity with other users in the dataset. It is implemented without using any external libraries, making it suitable for beginners who want to understand the fundamentals of recommendation systems and machine learning.

Features

- View available movies
- Rate movies on a scale of 1–5
- View previously rated movies
- Find the most similar user using Euclidean Distance
- Get personalized movie recommendations
- Menu-driven console interface

Algorithm Used

K-Nearest Neighbor (KNN)

The recommendation system uses the KNN concept to identify the user whose movie preferences are closest to the current user.

Euclidean Distance

Similarity between users is calculated using the Euclidean Distance formula:

Distance = √[(x₁−y₁)² + (x₂−y₂)² + ... + (xₙ−yₙ)²]

The user with the smallest distance is considered the nearest neighbor.

Dataset

The project contains:

- 10 Movies
- 5 Predefined Users
- Ratings from 1 to 5

Movies included:

- Avatar
- Titanic
- Inception
- Interstellar
- Iron Man
- Avengers Endgame
- Captain America
- John Wick
- Frozen
- Toy Story

How It Works

1. The user rates one or more movies.
2. The system compares the ratings with existing users.
3. Euclidean Distance is calculated for each user.
4. The most similar user is identified.
5. Unrated movies with ratings greater than or equal to 4 from the similar user are recommended.

Project Structure

- Movie List
- Training Dataset
- Rating Module
- Similarity Calculation Module
- Recommendation Engine
- User Interface Menu

Sample Output

Most Similar User Found: User4

Recommended Movies:

1. Interstellar
2. Captain America
3. John Wick

Advantages

- Easy to understand
- No external dependencies
- Demonstrates collaborative filtering concepts
- Suitable for academic and mini-project purposes

Future Improvements

- Multiple nearest neighbors (K > 1)
- Movie genre filtering
- Database integration
- Graphical User Interface (GUI)
- Larger movie datasets
- Advanced recommendation algorithms

Author

Ranjini

License

This project is developed for educational and learning purposes.
