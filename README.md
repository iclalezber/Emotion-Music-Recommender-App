# 🎶 Emotion-Based Music Recommender App

This is a web-based application that uses Natural Language Processing (NLP) to analyze user emotions from text input and recommend music that matches their mood. The app is built using Python and Flask, and leverages a pre-trained emotion classification model.

---

## 💡 Features

- 🎭 Emotion detection from user input (text-based)
- 🎵 Mood-matching music recommendations
- 🧠 Pre-trained NLP model with LabelEncoder support
- 🌐 Flask-based interactive web interface
- 📦 Clean and simple UI for quick access

---

## 🚀 How It Works

1. User types in a sentence describing their mood or current feeling.
2. The NLP model analyzes the emotional content.
3. Based on the predicted emotion, a song or playlist suggestion is generated.
4. The result is displayed with emotion label + music link.

---

## 🧰 Technologies Used

- Python
- Flask
- Scikit-learn
- Pandas & NumPy
- LabelEncoder
- HTML / CSS (frontend)

---

## 📁 Project Structure
```
Emotion_Music_Recommender_App/
│
├── app.py                   # Flask application entry point
├── emotion_model.pkl        # Trained emotion classifier model
├── label_encoder.pkl        # LabelEncoder for mapping emotion labels
├── songs.json               # JSON file with emotion-based music list
│
├── templates/               # HTML templates
│   └── index.html           # Main user interface
│
└── static/                  # Static files (CSS, JS, images)
    └── style.css            # Custom styles for the UI
```

---

## ▶️ Run the App

1. Clone the repo:

git clone https://github.com/iclalezber/Emotion-Music-Recommender-App.git
cd Emotion-Music-Recommender-App

2. Install dependencies:
pip install -r requirements.txt

3. Run the Flask app:
python app.py

Then open your browser and go to:
📍 http://127.0.0.1:5000

---

## 🧪 Example Input & Output
User Input:
"I feel so lonely and tired lately..."

Detected Emotion:
Sad

Recommended Music:
🎧 "Someone Like You – Adele"

## 📜 License
This project is open-source and licensed under the MIT License.
