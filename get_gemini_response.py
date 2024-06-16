import google.generativeai as genai

## Load Gemini pro vision model
model = genai.GenerativeModel('gemini-pro-vision')

def get_gemini_response(input,image,user_prompt):
    response=model.generate_content([input,image[0],user_prompt])
    return response.text