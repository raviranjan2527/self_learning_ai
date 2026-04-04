import json
import random
from langdetect import detect

# Load brain
try:
    with open("brain.json", "r") as f:
        knowledge = json.load(f)
except:
    knowledge = {}

# Auto fix structure
if "english" not in knowledge:
    knowledge["english"] = {}

if "hindi" not in knowledge:
    knowledge["hindi"] = {}

print("Auto Multilingual AI 😎")

# Language detect function
def detect_lang(text):
    try:
        lang = detect(text)
        if lang == "hi":
            return "hindi"
        else:
            return "english"
    except:
        return "english"


while True:
    user = input("You: ").lower()

    if user == "exit":
        break

    lang = detect_lang(user)

    if user in knowledge[lang]:
        print("AI:", random.choice(knowledge[lang][user]))
    else:
        print("AI: Mujhe nahi pata / I don't know.")
        ans = input("Teach: ")
        knowledge[lang][user] = [ans]

    with open("brain.json", "w") as f:
        json.dump(knowledge, f)
