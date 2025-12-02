# QuizBrain -- Python OOP Quiz Application

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)

A structured, Object-Oriented quiz application built for fun.
This project demonstrates clean OOP design, class interactions, input
handling, and data-driven question generation.

## 📌 Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Architecture](#architecture)
- [Project Structure](#project-structure)
- [Installation](#installation)
- [Usage](#usage)
- [How It Works](#how-it-works)
- [Future Improvements](#future-improvements)
- [License](#license)

## 📖 Overview

QuizBrain is a terminal-based quiz program that: - Loads question data
dynamically

- Builds question objects via a model class
- Organizes questions by difficulty
- Runs an interactive quiz loop
- Tracks score and progression

It combines **OOP concepts** such as: - Encapsulation

- Class composition
- Responsibility separation
- Data abstraction

## ✨ Features

- Difficulty-based quizzes (Easy, Medium, Hard)
- Clean OOP architecture (Question + QuizBrain classes)
- Input validation & error handling
- Scoring system with progress tracking
- Replay support
- Easily extensible question bank

## 🏗 Architecture

     ┌─────────────────────┐        ┌────────────────────────┐
     │    question_data    │        │     question_model     │
     │ (raw question list) │        │  (Question class)      │
     └─────────┬───────────┘        └───────────┬────────────┘
               │                                │
               ▼                                ▼
       Main Program (main.py)  ─────→  QuizBrain (quiz_brain.py)
               │                                │
               └──────────── Runs Quiz ─────────┘

## 📁 Project Structure

    QuizBrain/
    │
    ├── main.py
    ├── question_model.py
    ├── quiz_brain.py
    ├── data.py
    └── README.md

## ⚙ Installation

```bash
git clone https://github.com/sumayamahira/quiz_brain_project.git
cd quiz_brain_project
```

## ▶ Usage

```bash
python main.py
```

## 🔍 How It Works

1.  Question objects are created from `question_data`
2.  Questions are grouped by difficulty
3.  User selects a difficulty
4.  QuizBrain runs the quiz loop
5.  Score is calculated and shown at the end

## 🚀 Future Improvements

- GUI version\
- Multiple-choice questions\
- Timer-based mode\
- Online question API

## ✍️ Author

**Sumaya Mahira**

- 📩 Email: [eng.sumayamahira@gmail.com](eng.sumayamahira@gmail.com)

- 🌐 GitHub: [sumayamahira](https://github.com/sumayamahira)

- 🔗 LinkedIn: [sumaya-mahira](https://www.linkedin.com/in/sumaya-mahira)

Feel free to connect or follow my work on GitHub!

## 📄 License

Open Source
