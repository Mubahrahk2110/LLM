from google import genai
from dotenv import load_dotenv

load_dotenv()

client = genai.Client()

SYSTEM_PROMPT = '''
You are a learning assistant.
Explain concepts clearly and simply.
Use examples when useful.
if you are unsure, say you are unsure.

if the user asks any question related to mathematics, you should reply with "I am not able to answer questions related to mathematics."
'''

def get_response(prompt):
    interaction = client.interactions.create(
        model="gemini-3.5-flash-lite",
        system_instruction=SYSTEM_PROMPT,
        input=prompt
    )
    print(interaction.output_text)
input_prompt = input("Enter your prompt: ")
get_response(input_prompt)