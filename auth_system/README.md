# Auth System

A robust user authentication system for Hackotberfest2025 using Flask, OAuth2 (Google), and JWT.

## Features
- User registration and login
- OAuth2 login (Google)
- JWT-based session management
- User profile endpoint

## Setup
1. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
2. Set environment variables for Google OAuth2:
   - `GOOGLE_CLIENT_ID`
   - `GOOGLE_CLIENT_SECRET`
3. Run the app:
   ```bash
   python app.py
   ```

## Endpoints
- `POST /register` — Register with email/password
- `POST /login` — Login with email/password
- `GET /profile` — Get user profile (JWT required)
- `GET /login/google` — OAuth2 login (Google)
- `GET /login/google/callback` — OAuth2 callback

## Notes
- Uses SQLite for demo purposes
- Ready for future integration with dashboards, notifications, etc.
