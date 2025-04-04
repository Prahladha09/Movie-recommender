import os
from tabulate import tabulate

def save_user_rating(user_id, movie_name, rating):
  user_folder = f"E:\\ACADEMICS\\Semester_2\\Movie-Recommendation_prj\\user_history\\User_{user_id}"
  os.makedirs(user_folder, exist_ok=True)
  file_path = os.path.join(user_folder, "ratings.txt")
  clear_choice = input("Do you want to clear previous recommendations? (yes/no): ").strip().lower()
  if clear_choice == "yes":
     open(file_path, "w").close()  
  with open(file_path, 'a', encoding = 'utf-8') as file:
    file.write(f"Movie: {movie_name}, Rating: {rating}\n")