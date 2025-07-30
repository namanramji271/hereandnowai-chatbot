from openai import OpenAI
from dotenv import load_dotenv
import os
import requests

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")
model="gemini-2.5-flash-lite"
base_url="https://generativelanguage.googleapis.com/v1beta/openai"

client = OpenAI(base_url=base_url,api_key=api_key)

url = "https://raw.githubusercontent.com/hereandnowai/vac/refs/heads/master/prospectus-context.txt"
response =requests.get(url)

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path=os.path.join(script_dir,"profile-of-hereandnowai.txt")

with open(file_path, "wb") as f:
    f.write(response.content)