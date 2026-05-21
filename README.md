# 🤖 Jarvis — AI Voice Assistant

A Python-based voice assistant that responds to the wake word **"Jarvis"** and handles commands using OpenAI's GPT, speech recognition, and text-to-speech.

---

## Features

- Wake word detection ("Jarvis")
- Voice command recognition via Google Speech Recognition
- Text-to-speech responses using `pyttsx3`
- Opens websites (Google, Facebook, YouTube)
- Plays music from a custom library
- Fetches top news headlines via NewsAPI
- Falls back to GPT-4o-mini for general queries

---

## Requirements

- Python 3.8+
- A microphone

### Dependencies

Install all required packages:

```bash
pip install openai pyttsx3 SpeechRecognition requests pyaudio
```

> **Note:** `pyaudio` can be tricky to install on some systems.
> - **Windows:** `pip install pipwin && pipwin install pyaudio`
> - **macOS:** `brew install portaudio && pip install pyaudio`
> - **Linux:** `sudo apt-get install python3-pyaudio`

---

## Setup

**1. Clone the repository**

```bash
git clone https://github.com/your-username/jarvis-assistant.git
cd jarvis-assistant
```

**2. Add your API keys**

Open `main.py` and replace the placeholders:

```python
client = OpenAI(api_key="YOUR_OPENAI_API_KEY")
newsApi = "YOUR_NEWSAPI_KEY"
```

Get your keys here:
- OpenAI: https://platform.openai.com/api-keys
- NewsAPI: https://newsapi.org/

**3. Set up the music library**

Create a `musicLibrary.py` file in the project root:

```python
music = {
    "song_name": "https://youtube.com/link-to-song",
    "another_song": "https://youtube.com/link-to-another",
}
```

---

## Usage

```bash
python main.py
```

Once running, Jarvis listens for the wake word. Say **"Jarvis"** and wait for the confirmation, then give a command.

### Example Commands

| Command | Action |
|---|---|
| `"Open Google"` | Opens google.com in your browser |
| `"Open YouTube"` | Opens youtube.com in your browser |
| `"Open Facebook"` | Opens facebook.com in your browser |
| `"Play [song name]"` | Plays the song from your music library |
| `"News"` | Reads out top US headlines |
| Any other query | Answered by GPT-4o-mini |

---

## Project Structure

```
jarvis-assistant/
├── main.py            # Main application logic
├── musicLibrary.py    # Dictionary of song names and URLs
└── README.md
```

---

## Known Limitations

- Music playback only works for songs defined in `musicLibrary.py`
- News headlines are limited to US top stories (NewsAPI free tier)
- Speech recognition requires an active internet connection (Google API)
- Continuous listening may drain battery on laptops

---

## License

MIT License — feel free to use and modify.
