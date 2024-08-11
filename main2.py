from moviepy.editor import VideoFileClip, AudioFileClip
import speech_recognition as sr
from pydub import AudioSegment
from googletrans import Translator
from gtts import gTTS
import os
from dotenv import load_dotenv
import yt_dlp

# Load environment variables from .env file
load_dotenv()

# Paths for input, output, and temp files
EXTRACTED_AUDIO_PATH = "temp/extracted_audio.wav"
HINDI_AUDIO_PATH = "temp/hindi_audio.mp3"
OUTPUT_VIDEO_PATH = "output/output_hindi_dubbed_video.mp4"

def download_youtube_video(youtube_url, download_path="input/input_video.mp4"):
    print("Downloading video from YouTube using yt-dlp...")
    ydl_opts = {
        'format': 'best',
        'outtmpl': download_path,
    }
    try:
        with yt_dlp.YoutubeDL(ydl_opts) as ydl:
            ydl.download([youtube_url])
        print(f"Downloaded video to {download_path}")
        return download_path
    except Exception as e:
        print(f"Failed to download video: {e}")
        raise e

def extract_audio(video_path, output_audio_path):
    print("Extracting audio from video...")
    video = VideoFileClip(video_path)
    video.audio.write_audiofile(output_audio_path)

def transcribe_audio_to_text(audio_path):
    print("Transcribing audio to text...")
    recognizer = sr.Recognizer()
    audio = AudioSegment.from_file(audio_path)
    audio.export("temp.wav", format="wav")
    
    with sr.AudioFile("temp.wav") as source:
        audio_data = recognizer.record(source)
        text = recognizer.recognize_google(audio_data)
    
    os.remove("temp.wav")  # Clean up temporary file
    return text

def translate_text_to_hindi(text):
    print("Translating text to Hindi...")
    translator = Translator()
    translated = translator.translate(text, dest='hi')
    return translated.text

def text_to_speech(text, output_audio_path):
    print("Converting text to Hindi speech...")
    tts = gTTS(text=text, lang='hi')
    tts.save(output_audio_path)

def insert_audio_in_video(video_path, audio_path, output_video_path):
    print("Inserting Hindi dubbed audio into video...")
    video = VideoFileClip(video_path)
    audio = AudioFileClip(audio_path)
    
    new_video = video.set_audio(audio)
    new_video.write_videofile(output_video_path, audio_codec='aac')

def dub_video_to_hindi_from_youtube(youtube_url, output_video_path):
    # Step 1: Download Video from YouTube
    video_path = download_youtube_video(youtube_url)
    
    # Step 2: Extract Audio from Video
    extract_audio(video_path, EXTRACTED_AUDIO_PATH)
    
    # Step 3: Transcribe Audio to Text
    text = transcribe_audio_to_text(EXTRACTED_AUDIO_PATH)
    print(f"Transcribed Text: {text}")
    
    # Step 4: Translate Text to Hindi
    translated_text = translate_text_to_hindi(text)
    print(f"Translated Text: {translated_text}")
    
    # Step 5: Convert Translated Text to Hindi Speech
    text_to_speech(translated_text, HINDI_AUDIO_PATH)
    
    # Step 6: Insert Hindi Dubbed Audio in Video
    insert_audio_in_video(video_path, HINDI_AUDIO_PATH, output_video_path)
    
    print(f"Hindi dubbed video saved to {output_video_path}")

if __name__ == "__main__":
    youtube_url = os.getenv("YOUTUBE_URL")
    if not youtube_url:
        youtube_url = input("Enter the YouTube video URL: ")
    dub_video_to_hindi_from_youtube(youtube_url, OUTPUT_VIDEO_PATH)
  
