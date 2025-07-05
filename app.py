from flask import Flask, render_template, request
import joblib
import random
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

client_id = "9db6f089ff09421a98588bbe54cb6ea4"
client_secret = "c845be1e810b4073a5c716230f00ca86"

auth_manager = SpotifyClientCredentials(client_id=client_id, client_secret=client_secret)
sp = spotipy.Spotify(auth_manager=auth_manager)

app = Flask(__name__)

model = joblib.load("emotion_model.pkl")
label_encoder = joblib.load("label_encoder.pkl")

def search_songs_by_emotion(emotion, limit=5):
    emotion_keywords = {
        "joy": "happy upbeat feel good positive",
        "sadness": "sad heartbreak emotional melancholy",
        "anger": "angry aggressive rage hard rock",
        "fear": "scary suspenseful horror dark ambient",
        "surprise": "unexpected experimental twist progressive",
        "love": "romantic love ballad soft pop"
    }

    query = emotion_keywords.get(emotion.lower(), emotion)

    try:
        results = sp.search(q=query, type='track', limit=50)
        all_tracks = results['tracks']['items']
    except Exception as e:
        print("❌ Spotify API error:", e)
        all_tracks = []

    random.shuffle(all_tracks)

    songs = []
    for item in all_tracks[:limit]:
        name = item['name']
        artist = item['artists'][0]['name']
        url = item['external_urls']['spotify']
        image = item['album']['images'][0]['url'] if item['album']['images'] else None
        songs.append({"name": name, "artist": artist, "url": url, "image": image})
    return songs

@app.route("/", methods=["GET", "POST"])
def index():
    prediction = None
    songs = []
    user_text = ""
    empty_input_warning = False

    if request.method == "POST":
        user_text = request.form["text"].strip()

        if not user_text:
            empty_input_warning = True
        else:
            prediction_encoded = model.predict([user_text])[0]
            prediction = label_encoder.inverse_transform([prediction_encoded])[0]
            songs = search_songs_by_emotion(prediction)

    return render_template("index.html",
                           prediction=prediction,
                           songs=songs,
                           user_text=user_text,
                           empty_input_warning=empty_input_warning)

if __name__ == "__main__":
    app.run(debug=True)