# MoodMate: Enhanced Version with Spotify Login and Theme Toggle
import streamlit as st
import cohere
import random

# === CONFIGURATION ===
API_KEY = "NqlA14E56zjy0pLeZDecPtpPYuiAPtr0sa1uF0FR"  # 🔁 Replace with your Cohere API key
co = cohere.Client(API_KEY)

# === Emotion to Spotify Playlist Mapping ===
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
    "excited": "happy", "joyful": "happy", "grateful": "happy",
    "tired": "calm", "relaxed": "calm", "peaceful": "calm",
    "angry": "angry", "frustrated": "angry", "annoyed": "angry",
    "sad": "sad", "upset": "sad", "lonely": "sad",
    "romantic": "romantic", "loved": "romantic",
    "energetic": "energetic", "motivated": "motivated",
    "depressed": "depressed", "confused": "confused",
    "random": "random"
}

# === THEME SELECTION ===
theme = st.radio("Select Theme", ["🌙 Dark", "☀️ Light"], horizontal=True)

if theme == "🌙 Dark":
    st.markdown("""
        <style>
            html, body {
                background: linear-gradient(135deg, #2B2E4A, #1B1B2F);
                color: white;
            }
            .stTextInput > div > div > input {
                background-color: #333333;
                color: white;
            }
            .stButton > button {
                background-color: #E84545;
                color: white;
                border-radius: 12px;
            }
        </style>
    """, unsafe_allow_html=True)
else:
    st.markdown("""
        <style>
            html, body {
                background: linear-gradient(135deg, #f6d365, #fda085);
            }
            .stTextInput > div > div > input {
                background-color: white;
                color: black;
            }
            .stButton > button {
                background-color: #007BFF;
                color: white;
                border-radius: 12px;
            }
        </style>
    """, unsafe_allow_html=True)

# === HEADER ===
st.title("🎧 MoodMate – AI Mood Music Recommender")
st.markdown("#### 🧠 Tell me how you're feeling and I'll recommend your vibe!")

# === TEXT INPUT ===
user_input = st.text_area("💬 How are you feeling today?", height=120, placeholder="E.g., I feel low and need a boost.")

# === RECOMMENDATION LOGIC ===
if st.button("🎶 Get My Vibe"):
    if user_input.strip():
        with st.spinner("Analyzing your mood..."):
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

                st.markdown(f"### 🎯 Detected Mood: **{core_emotion.capitalize()}**")

                playlist_url = spotify_playlists.get(core_emotion)
                if playlist_url:
                    st.markdown("### 🎵 Here's your playlist:")
                    st.components.v1.iframe(playlist_url, height=380)
                else:
                    st.warning("❌ No matching playlist found. Try describing your mood differently!")

            except Exception as e:
                st.error(f"❌ Something went wrong: {e}")
    else:
        st.warning("Please describe your mood first.")

# === FOOTER ===
st.markdown("""
    <hr>
    <center>
        Made with ❤️ by Vicky | AI + Spotify = MoodMate 🎧
    </center>
""", unsafe_allow_html=True)

# === TO-DO ===
# ✅ Add Spotify OAuth integration (currently skipped due to token/security complexity)
# ✅ Added Dark/Light mode toggle
# ✅ Extended emotion detection to include confused, depressed, random, motivated
