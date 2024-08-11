from moviepy.editor import VideoFileClip, AudioFileClip
import speech_recognition as sr
from pydub import AudioSegment
from googletrans import Translator
from gtts import gTTS
import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Paths for input, output, and temp files
INPUT_VIDEO_PATH = "input/input_video.mp4"
EXTRACTED_AUDIO_PATH = "temp/extracted_audio.wav"
HINDI_AUDIO_PATH = "temp/hindi_audio.mp3"
OUTPUT_VIDEO_PATH = "output/output_hindi_dubbed_video.mp4"

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

def dub_video_to_hindi_from_uploaded(video_path, output_video_path):
    # Step 1: Extract Audio from Video
    extract_audio(video_path, EXTRACTED_AUDIO_PATH)
    
    # Step 2: Transcribe Audio to Text
    text = transcribe_audio_to_text(EXTRACTED_AUDIO_PATH)
    print(f"Transcribed Text: {text}")
    
    # Step 3: Translate Text to Hindi
    translated_text = translate_text_to_hindi(text)
    print(f"Translated Text: {translated_text}")
    
    # Step 4: Convert Translated Text to Hindi Speech
    text_to_speech(translated_text, HINDI_AUDIO_PATH)
    
    # Step 5: Insert Hindi Dubbed Audio in Video
    insert_audio_in_video(video_path, HINDI_AUDIO_PATH, output_video_path)
    
    print(f"Hindi dubbed video saved to {output_video_path}")

if __name__ == "__main__":
    video_path = INPUT_VIDEO_PATH
    dub_video_to_hindi_from_uploaded(video_path, OUTPUT_VIDEO_PATH)
