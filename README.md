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

