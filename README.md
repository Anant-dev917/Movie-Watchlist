# 🎬 Movie Watchlist

## Overview
The Movie Watchlist Web App is a Flask-based web application that allows users to create and manage their personalized movie watchlists. Users can add movies, view details such as director names, cast, and genres, and even embed trailer links or other relevant videos. The app provides a user-friendly interface with both light and dark mode options for enhanced viewing comfort.

## 🚀 Features
- **User Authentication**
  - Secure sign-up and login system.
  - Passwords are encrypted using `pbkdf2_sha256` for user privacy.
- **Personalized movie lists**
  - Users can add any number of movies to their watchlist.
  - Each movie includes details like title, director, cast, genre, and a summary.
  - Movies are displayed on a personalized page once added.
- **Trailer Embeds**
  - Users can submit an embed link (e.g., YouTube trailer), which will be displayed alongside the movie details.
- **Dark Mode / Light Mode**
  - Users can switch between dark and light themes.
  - CSS variables and styling are used to dynamically change the theme without reloading the page.
- **Responsive Design**
  - The layout is responsive and adapts well to different screen sizes.

## 🛠️ Tech Stack
- Frontend
  - HTML5, CSS3
  - WTForms (for handling form inputs and validation)
  - CSS variables (for theme toggling)
- Backend
  - Python 3
  - Flask
  - jinja2 templating
- Database
  - MongoDB (used to store user accounts and movie data)
- Authentication and security
  - `Flask-Login` for session management
  - `passlib` (`pbkdf2_sha256`) for password hashing

## 🧪 How to Run Locally
1. Clone the Repository
   - ```
     git clone https://github.com/Anant-dev917/Movie-Watchlist.git
     cd movie-watchlist
     ```
2. Create a Virtual Environment
   - ```
     python -m venv venv
     source venv/bin/activate  # On Windows use `venv\Scripts\activate`
     ```
3. Install Dependencies
   - `pip install -r requirements.txt`
4. Set Up Environment Variables
   Create a `.env` file (or use environment variables) to include:
   - SECRET_KEY
   - MONGO_URI
5. Run the app
   `flask run`
6. Visit `http://localhost:5000` in your browser.

## 💡 Future Improvements
- Edit/delete movie entries

- Add image upload or movie posters

- Add movie ratings and reviews

## 📸 Screenshots
![User personalized movie watchlist](https://github.com/user-attachments/assets/2c063ce7-1d98-4b4a-a400-085008800dee)

![/2](https://github.com/user-attachments/assets/2e851cd3-b40d-4a6f-9b44-ed678153cb29)




## 🧑‍💻 Author
- Anant Shaynam
- [My Linkedin](https://www.linkedin.com/in/anant-shaynam-80b0b3250/) | [My portfolio](https://portfolio-8mjp.onrender.com/)

