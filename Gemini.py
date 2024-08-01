import google.generativeai as genai
import os

genai.configure(api_key=os.environ["AIzaSyArr-AcewxlEklUiC5ivMAvSJ5X_QJkKMo"])
def main():
   
    model = genai.GenerativeModel('gemini-1.0-pro-latest')
    response = model.generate_content("The opposite of hot is")
    print(response.text)
    

if __name__ ==