import os
import sys
from openai import OpenAI

audio_file_path = sys.argv[1]

client = OpenAI()
client.api_key = os.getenv("OPENAI_API_KEY")

audio_file= open(audio_file_path, "rb")
transcription = client.audio.transcriptions.create(
  model="whisper-1", 
  file=audio_file
)

print(transcription.text)
