# importing necessary libraries
import numpy as np
import pandas as pd
from tabulate import tabulate
import movie_recommender
import user_history_saver
import user_movie_ratings_saver

# data collection 
telugu_movie_dataset = pd.read_csv('E:\\ACADEMICS\\Semester_2\\Movie-Recommendation_prj\\assets\\data-sets\\TeluguMovies_dataset.csv')
all_movies_dataset = pd.read_csv('E:\\ACADEMICS\\Semester_2\\Movie-Recommendation_prj\\assets\\data-sets\\imdb_top_1000.csv')

# data pre-processing
# removing unwanted columns and renaming the columns of all data-set's in a same way
telugu_movie_dataset.drop(columns=['Unnamed: 0'], inplace=True)
all_movies_dataset.rename(columns = {'Series_Title':'Movie', 'IMDB_Rating': 'Rating'}, inplace = True)

# getting different types of Genres of a dataset into a list
split_genres = telugu_movie_dataset['Genre'].str.split(',')
all_genres = split_genres.explode().str.strip()
telugu_movie_genres = list(all_genres.unique())

split_genres = all_movies_dataset['Genre'].str.split(',')
all_genres = split_genres.explode().str.strip()
all_movie_genres = list(all_genres.unique())


# main code
proceed = 'yes'
while str.lower(proceed) == 'yes':
    print("\n" + "="*50)
    print("🎬 𝗪𝗲𝗹𝗰𝗼𝗺𝗲 𝘁𝗼 𝗠𝗼𝘃𝗶𝗲 𝗥𝗲𝗰𝗼𝗺𝗺𝗲𝗻𝗱𝗮𝘁𝗶𝗼𝗻 𝗦𝘆𝘀𝘁𝗲𝗺 🎥")
    print("="*50)

    # Get user details
    user_id = input("\n🆔 Please enter your User ID: ")

    # Ask if the user wants recommendations
    print("\n🤔 Don't know what movie to watch?")
    choice = input("➡️ Type 'yes' to get a movie recommendation or 'no' to exit: ")

    if str.lower(choice) == 'yes':
        print("\n🌍 Choose your preferred movie language:")
        print("1️⃣ Telugu\n2️⃣ Any language")
        language = int(input("➡️ Enter your choice (1/2): "))

        print("\n🎯 How would you like me to recommend movies?")
        print("1️⃣ Based on Rating\n2️⃣ Based on Genre and Rating")
        way = int(input("➡️ Enter your choice (1/2): "))

        number = int(input("\n🎬 How many movies do you want me to recommend? "))

        if way == 1:
            rating = float(input("\n🎬 Excited to watch a movie? Set your preferred rating range (⭐ 0 - 10 ⭐):"))
            movies_recommend = movie_recommender.Recommended_movies(telugu_movie_dataset if language == 1 else all_movies_dataset, way, rating, number_of_movies=number)
            
            print("\n🎥 𝗥𝗲𝗰𝗼𝗺𝗺𝗲𝗻𝗱𝗲𝗱 𝗠𝗼𝘃𝗶𝗲𝘀 📽️")
            print(tabulate(movies_recommend, headers="keys", tablefmt="fancy_grid"))

            # Ask if user wants to save recommendations
            save_rec = input("\n💾 Do you want to save these recommendations? (yes/no): ")
            if str.lower(save_rec) == 'yes':
                user_history_saver.save_recommendations(user_id, movies_recommend)
            else:
                print("❌ Recommendations not saved!")

        elif way == 2:
            rating = float(input("\n🎬 Excited to watch a movie? Set your preferred rating range (⭐ 0 - 10 ⭐):"))

            print("\n🎭 Available Genres:")
            print(telugu_movie_genres if language == 1 else all_movie_genres)


            genres = input("\n🎬 Enter the genres you are interested in (comma-separated): ")
            genres = [g.strip().capitalize() for g in genres.split(',')]

            movies_recommend = movie_recommender.Recommended_movies(telugu_movie_dataset if language == 1 else all_movies_dataset, way, rating, Genre=genres, number_of_movies=number)

            print("\n🎥 𝗥𝗲𝗰𝗼𝗺𝗺𝗲𝗻𝗱𝗲𝗱 𝗠𝗼𝘃𝗶𝗲𝘀 📽️")
            print(tabulate(movies_recommend, headers="keys", tablefmt="fancy_grid"))

            # Ask if user wants to save recommendations
            save_rec = input("\n💾 Do you want to save these recommendations? (yes/no): ")
            if str.lower(save_rec) == 'yes':
                user_history_saver.save_recommendations(user_id, movies_recommend)
            else:
                print("❌ Recommendations not saved!")

    elif str.lower(choice) == 'no':
        print("\n😊 Thank you for using the Movie Recommendation System!")
        break  # Exit the loop

    else:
        print("\n❌ Invalid input. Please enter 'yes' or 'no'.")

    # Ask if the user wants to rate a movie
    print("\n⭐ Do you want to rate a movie?")
    rate_movie = input("➡️ Type 'yes' to rate or 'no' to skip: ")
    
    if str.lower(rate_movie) == 'yes':
        movie_name = input("\n🎬 Enter the movie name: ")
        rating = float(input("⭐ Enter your rating (0-10): "))
        user_movie_ratings_saver.save_user_rating(user_id, movie_name, rating)
    else:
        print("🎭 No movie rated!")

    # Ask if the user wants to continue
    print("\n🔄 Do you want to check new movie recommendations?")
    proceed = input("➡️ Type 'yes' to continue or 'no' to exit: ")
    
    if str.lower(proceed) == 'no':
        print("\n🎉 Thank you for using the system! Have a great day! 😊")
        break  # Exit the loop
