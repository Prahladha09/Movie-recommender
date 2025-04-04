## 🎬 **Movie Recommendation System**  

### 📌 **Project Description**  
The **Movie Recommendation System** suggests movies to users based on their preferences, including rating and genre. Users can also save recommendations and rate movies along with saving them.  

---

## 📂 **Project Structure**  
```
CollegeName_FullName_MovieRecommendation/
├── src/
│   ├── main.py  # Main script to run the recommendation system
│   ├── recommend.py  # Functions for recommending movies
│   ├── storage.py  # Functions for saving recommendations and ratings
│   ├── dataset.py  # Loads the movie datasets
├── assets/  
│   ├── sample_data.csv  # Sample movie dataset (if needed)
│   ├── genres_list.txt  # List of movie genres (if needed)
├── requirements.txt  # Required dependencies
├── README.md  # Project documentation
```

---

## 🚀 **Installation & Setup**  

1️⃣ **Clone the repository**  
```
git clone https://github.com/yourusername/MovieRecommendationSystem.git
cd MovieRecommendationSystem
```

2️⃣ **Install dependencies**  
```
pip install -r requirements.txt
```

3️⃣ **Run the program**  
```
python src/main.py
```

---

## ⚙️ **Design Choices**  

### 🏗 **Programming language and Libraries used Used**  
- **Python** – Core programming language  
- **Pandas & NumPy** – For data processing  
- **Tabulate** – To display recommendations in a structured format  
- **OS module** – For file handling and user-specific storage  

### 🎯 **Recommendation Approaches**  
1️⃣ **Rating-based Recommendation**  
   - Users enter a preferred rating, and the system suggests top-rated movies (number of movies suggest is based on user).  

2️⃣ **Genre + Rating Recommendation**  
   - Users select genres (e.g., Action, Comedy) and a rating to receive customized recommendations.  

---

## 🎭 **Features & Functionality**  

✅ **Movie Recommendations** – Get movie suggestions based on rating and genre preferences.  
✅ **Personalized Storage** – Each user's recommendations and ratings are stored in a dedicated folder.  
✅ **Rating System** – Users can rate movies and store them in a dedicated folder.  
✅ **Interactive UI** – The system prompts users step-by-step, with visually appealing emojis and separators.  

---

## 📚 **Key Learnings**  
🔹 Revisited the conepts of **Pandas & NumPy** for data handling.  
🔹 Implementing **file handling in Python** for personalized storage.  
🔹 Improving **user experience** with better input prompts and formatting.  
🔹 Learnt how to use user based modules and packages  
