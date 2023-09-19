# Mille Bornes Game

A modern implementation of the classic card game, Mille Bornes. This project utilizes Angular for the frontend and Python for the backend, with data storage in SQLite.

# Game Outline:

1. **Players**: Typically, two players or two pairs of players.
2. **Cards**: 106 cards comprising Distance, Hazard, Remedy, Safety, and Speed Limit cards.
3. **Objective**: Players aim to be the first to travel 1000 miles (the game's name means a "thousand milestones" in French).

## Table of Contents

1. [Features](#features)
2. [Getting Started](#getting-started)
3. [Project Structure](#project-structure)
4. [Contributing](#contributing)
5. [License](#license)

## Features

- 🚗 Classic Mille Bornes gameplay.
- 🖥️ Intuitive and modern user interface.
- 📊 Persistent game stats stored in SQLite.
- 🌍 Multiplayer support through web services.

## Getting Started

### Prerequisites

- Node.js and npm for frontend development.
- Python 3.x for backend development.

### Installation

1. **Frontend**:
  ```bash
  cd frontend
  npm install
  ng serve
  ```
  Open `http://localhost:4200` in your browser.

2. **Backend**:
  ```bash
  cd backend
  pip install -r requirements.txt
  python main.py
  ```

### Database Setup

Navigate to the `backend/db` directory and run the `db_setup.py` script:

```bash
cd backend/db
python db_setup.py
```

This will initialize the SQLite database with the necessary tables.

## Project Structure

- `/frontend/mille-bornes` - Contains all frontend code, based on Angular.
 - `/src/app/` - Angular components, services, models, etc.
 - `/src/assets/` - Images, fonts, and other static assets.

- `/backend/` - Contains all backend Python code.
 - `/mille_bornes/` - Core game logic.
 - `/db/` - Database setup script and SQLite3 database file.
 - `/services/` - Web services and API routes.

For more details, refer to the [folder structure guide](#).
