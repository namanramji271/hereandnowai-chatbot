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

text_path=file_path

# UTF-8 is a character encoding that represents text in a way that's compatible with ASCII and can also handle a wide range of characters from different languages
try:
    with open(text_path,"r",encoding="utf-8") as file: 
        text_lines = file.readlines()
        text_content="\n".join([line.strip() for line in text_lines if line.strip()])
except Exception as e:
    print("Error reading the text file {e}")
    text_content = "Error extracting text from text file"

def get_response(message,history):
    system_prompt = f"You are Caramel AI assistant built by HERE AND NOW AI. Answer the user's only on the following context:\n\n{text_content}"
    messages =[{"role":"system","content":system_prompt}]
    messages.extend(history)
    messages.append({"role":"user","content":message})
    response = client.chat.completions.create(model=model,messages=messages)
    ai_response = response.choices[0].message.content
    return ai_response

print(get_response("Hello Caramel, who is the CTO of Here and now AI",[]))