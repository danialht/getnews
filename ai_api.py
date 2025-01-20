import google.generativeai as googlegenai

class Genai():
    def __init__(self, api_key):
        googlegenai.configure(api_key=api_key)
        self.model = googlegenai.GenerativeModel("gemini-1.5-flash")
    
    def query(self, prompt):
        return self.model.generate_content(prompt).text
    