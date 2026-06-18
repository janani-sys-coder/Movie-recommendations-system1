# Personalized Movie Recommendation System
# Machine Learning (KNN) - No External Libraries

movies = [
    "Avatar",
    "Titanic",
    "Inception",
    "Interstellar",
    "Iron Man",
    "Avengers Endgame",
    "Captain America",
    "John Wick",
    "Frozen",
    "Toy Story"
]

# Training Data
training_data = {
    "User1": [5, 1, 5, 4, 5, 5, 4, 3, 1, 1],
    "User2": [4, 2, 5, 5, 4, 4, 5, 4, 1, 1],
    "User3": [1, 5, 2, 1, 1, 1, 2, 2, 5, 4],
    "User4": [5, 1, 4, 5, 5, 5, 5, 4, 1, 1],
    "User5": [2, 5, 1, 2, 1, 1, 1, 2, 5, 5]
}

user_ratings = [0] * len(movies)

def show_movies():
    print("\n========== AVAILABLE MOVIES ==========")
    for i in range(len(movies)):
        print(str(i + 1) + ".", movies[i])

def rate_movie():
    show_movies()

    try:
        choice = int(input("\nEnter movie number: ")) - 1

        if choice < 0 or choice >= len(movies):
            print("Invalid movie number.")
            return

        rating = int(input("Rate this movie (1-5): "))

        if rating < 1 or rating > 5:
            print("Rating must be between 1 and 5.")
            return

        user_ratings[choice] = rating
        print("Rating saved successfully!")

    except:
        print("Invalid input.")

def view_ratings():
    print("\n========== YOUR RATINGS ==========")

    found = False

    for i in range(len(movies)):
        if user_ratings[i] > 0:
            print(movies[i], ":", user_ratings[i])
            found = True

    if not found:
        print("No ratings available.")

def euclidean_distance(user1, user2):
    total = 0

    for i in range(len(user1)):
        total += (user1[i] - user2[i]) ** 2

    return total ** 0.5

def recommend_movies():

    if max(user_ratings) == 0:
        print("\nPlease rate some movies first.")
        return

    nearest_user = ""
    min_distance = float("inf")

    for user, ratings in training_data.items():

        distance = euclidean_distance(user_ratings, ratings)

        if distance < min_distance:
            min_distance = distance
            nearest_user = user

    print("\nMost Similar User Found:", nearest_user)

    recommendations = []

    nearest_ratings = training_data[nearest_user]

    for i in range(len(movies)):

        if user_ratings[i] == 0 and nearest_ratings[i] >= 4:
            recommendations.append((movies[i], nearest_ratings[i]))

    print("\n========== RECOMMENDED MOVIES ==========")

    if len(recommendations) == 0:
        print("No recommendations available.")
        return

    count = 1

    for movie, score in recommendations:
        print(str(count) + ".", movie,
              "| Predicted Interest Score:", score)
        count += 1

while True:

    print("\n")
    print("=" * 50)
    print("PERSONALIZED MOVIE RECOMMENDATION SYSTEM")
    print("=" * 50)

    print("1. Show Available Movies")
    print("2. Rate a Movie")
    print("3. Get Recommendations")
    print("4. View My Ratings")
    print("5. Exit")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        show_movies()

    elif choice == "2":
        rate_movie()

    elif choice == "3":
        recommend_movies()

    elif choice == "4":
        view_ratings()

    elif choice == "5":
        print("\nThank you for using the system!")
        break

    else:
        print("Invalid choice. Please try again.")
