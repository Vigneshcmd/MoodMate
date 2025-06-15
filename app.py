import streamlit as st
import cohere
import random

# === API CONFIG ===
API_KEY = "NqlA14E56zjy0pLeZDecPtpPYuiAPtr0sa1uF0FR"
co = cohere.Client(API_KEY)

# === SPOTIFY PLAYLIST MAP ===
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
    "joyful": "https://open.spotify.com/embed/playlist/37i9dQZF1DWYBO1MoTDhZI",
    "pleasant": "https://open.spotify.com/embed/playlist/37i9dQZF1DX4WYpdgoIcn6",
    "anxious": "https://open.spotify.com/embed/playlist/37i9dQZF1DWVrtsSlLKzro",
    "irritated": "https://open.spotify.com/embed/playlist/37i9dQZF1DWU4EQPjP9ZpS",
    "not sure": "https://open.spotify.com/embed/playlist/37i9dQZF1DX1s9knjP51Oa",
    "don't know": "https://open.spotify.com/embed/playlist/37i9dQZF1DX2sUQwD7tbmL",
    "not happy not sad": "https://open.spotify.com/embed/playlist/37i9dQZF1DX3rxVfibe1L0",
    "random": random.choice([
        "https://open.spotify.com/embed/playlist/37i9dQZF1DWXT8uSSn6PRy",
        "https://open.spotify.com/embed/playlist/37i9dQZF1DX4UtSsGT1Sbe"
    ])
}

# === EMOTION MAP ===
emotion_map = {
    "excited": "happy", "joyful": "joyful", "grateful": "happy",
    "tired": "calm", "relaxed": "calm", "peaceful": "calm", "pleasant": "pleasant",
    "angry": "angry", "frustrated": "angry", "annoyed": "angry", "irritated": "irritated",
    "sad": "sad", "upset": "sad", "lonely": "sad",
    "romantic": "romantic", "loved": "romantic",
    "energetic": "energetic", "motivated": "motivated",
    "depressed": "depressed", "confused": "confused", "anxious": "anxious",
    "not sure": "not sure", "don't know": "don't know", "not happy not sad": "not happy not sad",
    "random": "random"
}

# === PAGE CONFIG ===
st.set_page_config(page_title="MoodMate 🎧", layout="wide")

# === CUSTOM CSS ===
st.markdown("""
<style>
body {
    background-color: #1e1e2f;
    font-family: 'Poppins', sans-serif;
    color: #f8f9fa;
}
h1, h2, h3 {
    font-family: 'Orbitron', sans-serif;
    color: #f1f1f1;
}
.big-title {
    font-size: 56px;
    font-weight: 800;
    letter-spacing: 3px;
    margin-bottom: 0;
    color: #fca311;
}
.subtle {
    font-size: 18px;
    color: #adb5bd;
}
.stTextArea > div > textarea {
    background-color: #2a2a3b;
    color: #ffffff;
    font-size: 18px;
    border: 1px solid #444;
    border-radius: 10px;
}
button[kind="primary"] {
    background: linear-gradient(45deg, #ff6f61, #ffcc70);
    border: none;
    border-radius: 10px;
    color: white;
    padding: 10px 20px;
    font-weight: bold;
    font-size: 16px;
    box-shadow: 0 4px 14px rgba(255, 105, 135, .3);
}
</style>
<link href="https://fonts.googleapis.com/css2?family=Orbitron:wght@600&family=Poppins&display=swap" rel="stylesheet">
""", unsafe_allow_html=True)

# === HEADER ===
st.markdown("<h1 class='big-title'>MoodMate</h1>", unsafe_allow_html=True)
st.markdown("<p class='subtle'>AI-Powered Music Mood Recommender 🎧</p>", unsafe_allow_html=True)
st.markdown("---")

# === USER INPUT ===
user_input = st.text_area("💬 What's your current mood or feeling?", height=150, placeholder="Type how you feel...")

# === ANALYSIS ===
if st.button("🔍 Analyze & Recommend"):
    if user_input.strip():
        with st.spinner("Thinking like your emotional bestie..."):
            prompt = f"From this text, extract a single word that reflects the mood (happy, sad, calm, romantic, energetic, confused, depressed, etc.):\n\n\"{user_input.strip()}\""
            try:
                response = co.generate(
                    model="command-r-plus",
                    prompt=prompt,
                    max_tokens=8,
                    temperature=0.6
                )
                raw_emotion = response.generations[0].text.strip().lower()
                mapped_emotion = emotion_map.get(raw_emotion, "random")

                st.success(f"✨ Mood Detected: **{mapped_emotion.title()}**")
                st.markdown("### 🎵 Your Vibe Tracklist")
                st.components.v1.iframe(spotify_playlists[mapped_emotion], height=400)

            except Exception as e:
                st.error(f"Something went wrong 😔: {e}")
    else:
        st.warning("Please describe your mood to get a song vibe!")

# === FOOTER ===
st.markdown("---")
st.markdown("<center><span class='subtle'>Designed with ❤️ by Vicky | MoodMate 2025</span></center>", unsafe_allow_html=True)
