import streamlit as st
import cohere
import random

# === CONFIG ===
API_KEY = "NqlA14E56zjy0pLeZDecPtpPYuiAPtr0sa1uF0FR"  # Replace with your Cohere key
co = cohere.Client(API_KEY)

# === Emotion Mapping ===
spotify_playlists = {
    "happy": "https://open.spotify.com/embed/playlist/37i9dQZF1DXdPec7aLTmlC",
    "sad": "https://open.spotify.com/embed/playlist/37i9dQZF1DX7qK8ma5wgG1",
    "angry": "https://open.spotify.com/embed/playlist/37i9dQZF1DWYxwmBaMqxsl",
    "calm": "https://open.spotify.com/embed/playlist/37i9dQZF1DWVV27DiNWxkR",
    "romantic": "https://open.spotify.com/embed/playlist/37i9dQZF1DWXbttAJcbphz",
    "energetic": "https://open.spotify.com/embed/playlist/37i9dQZF1DX76Wlfdnj7AP",
    "motivated": "https://open.spotify.com/embed/playlist/37i9dQZF1DXc6IFF23C9jj",
    "confused": "https://open.spotify.com/embed/playlist/37i9dQZF1DWUvZBXGjNCU4",
    "depressed": "https://open.spotify.com/embed/playlist/37i9dQZF1DX3YSRoSdA634",
    "random": random.choice([
        "https://open.spotify.com/embed/playlist/37i9dQZF1DX2sUQwD7tbmL",
        "https://open.spotify.com/embed/playlist/37i9dQZF1DX1s9knjP51Oa"
    ])
}

emotion_map = {
    "excited": "happy", "joyful": "happy", "grateful": "happy", "pleasant": "happy",
    "tired": "calm", "relaxed": "calm", "peaceful": "calm", "not happy not sad": "calm",
    "angry": "angry", "frustrated": "angry", "annoyed": "angry", "irritated": "angry",
    "sad": "sad", "upset": "sad", "lonely": "sad",
    "romantic": "romantic", "loved": "romantic",
    "energetic": "energetic", "motivated": "motivated",
    "depressed": "depressed", "confused": "confused", "anxious": "confused",
    "random": "random"
}

# === STYLING ===
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;500;700&family=Rubik:wght@400;600&display=swap');

    html, body, .stApp {
        background: linear-gradient(to right, #fdfbfb, #ebedee);
        font-family: 'Rubik', sans-serif;
        color: #2c2c2c;
    }

    .title {
        text-align: center;
        font-size: 3em;
        font-family: 'Poppins', sans-serif;
        font-weight: 700;
        color: #5e60ce;
        margin-top: 20px;
    }

    .subtitle {
        text-align: center;
        font-size: 1.2em;
        font-weight: 400;
        color: #5e60ce;
        margin-bottom: 30px;
    }

    .stTextInput textarea, .stTextArea textarea {
        background-color: #ffffff;
        border-radius: 10px;
        border: 2px solid #cdb4db;
        padding: 12px;
        font-size: 16px;
        color: #333;
    }

    .stButton > button {
        background-color: #5e60ce;
        color: white;
        padding: 12px 28px;
        font-size: 18px;
        border-radius: 12px;
        border: none;
        transition: 0.3s ease;
        box-shadow: 0px 4px 15px rgba(0,0,0,0.1);
    }

    .stButton > button:hover {
        background-color: #6930c3;
        transform: scale(1.05);
    }

    .result-text {
        font-size: 22px;
        font-weight: 600;
        color: #6930c3;
        padding-top: 20px;
    }

    iframe {
        border-radius: 16px;
        margin-top: 20px;
        box-shadow: 0px 8px 20px rgba(0,0,0,0.1);
    }

    footer {
        margin-top: 40px;
        text-align: center;
        font-size: 14px;
        color: #555;
    }
    </style>
""", unsafe_allow_html=True)

# === TITLE ===
st.markdown('<div class="title">MoodMate 🎧</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle">Your AI-powered music buddy that matches your vibe ✨</div>', unsafe_allow_html=True)

# === USER INPUT ===
user_input = st.text_area("How are you feeling today?", height=120, placeholder="e.g., I feel anxious and need some clarity.")

# === BUTTON & RESPONSE ===
if st.button("🎶 Recommend Me Music"):
    if user_input.strip():
        with st.spinner("Analyzing your emotion..."):
            try:
                prompt = f"Identify the emotion behind this sentence in one word (like happy, sad, angry, calm, romantic, energetic, confused, depressed):\n\n\"{user_input.strip()}\"\n\nOnly reply with the emotion word."
                response = co.generate(
                    model="command-r-plus",
                    prompt=prompt,
                    max_tokens=10,
                    temperature=0.5
                )
                raw_emotion = response.generations[0].text.strip().lower()
                core_emotion = emotion_map.get(raw_emotion, raw_emotion)

                st.markdown(f"<div class='result-text'>🎯 Detected Mood: <b>{core_emotion.capitalize()}</b></div>", unsafe_allow_html=True)

                playlist_url = spotify_playlists.get(core_emotion)
                if playlist_url:
                    st.components.v1.iframe(playlist_url, height=380)
                else:
                    st.warning("No playlist found. Try expressing your mood in simpler words.")
            except Exception as e:
                st.error(f"Something went wrong: {e}")
    else:
        st.warning("Please describe your mood to get a music suggestion.")

# === FOOTER ===
st.markdown("""
    <footer>
        Made with 💜 by Vicky | AI x Spotify = Pure Vibes 💫
    </footer>
""", unsafe_allow_html=True)
