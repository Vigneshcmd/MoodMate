# MoodMate
# 🎧 MoodMate – AI Mood-Based Music Recommender

MoodMate is a smart, emotion-aware music recommender built using **Streamlit** and Cohere's NLP. It analyzes how you're feeling from your text and plays a matching Spotify playlist that fits your current mood.

---

## 🚀 Features

- 🧠 **AI Mood Detection** from natural language input
- 🎵 **Spotify Playlist Recommendations** based on mood
- 🌗 **Dark & Light Theme Toggle** with animated switch
- 💬 Supports moods like *happy, sad, angry, calm, romantic, energetic, motivated, confused, depressed,* and *random*
- 🎨 Clean, aesthetic, and responsive UI

---

## ⚙️ How It Works

1. ✍️ User types how they feel (e.g., *“I feel motivated to finish my goals!”*)
2. 🤖 AI detects the emotion using Cohere
3. 🎧 The app recommends a Spotify playlist via embedded iframe

---

## 🛠 Built With

- **Python**
- **Streamlit**
- **Cohere NLP**
- **Spotify Embed**
- **Custom CSS for themes & UI styling**

---

## 📦 Setup

```bash
git clone https://github.com/vigneshcmd/MoodMate.git
cd MoodMate
pip install -r requirements.txt
streamlit run app.py
