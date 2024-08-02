import google.generativeai as genai
import os

# Charger la clé API à partir d'un fichier de configuration
with open("config.txt", "r") as f:
    api_key = f.read().strip()

genai.configure(api_key=api_key)
def get_response(request):
   
    model = genai.GenerativeModel('gemini-1.5-flash')
    response = model.generate_content(request)
    return response.text
    
