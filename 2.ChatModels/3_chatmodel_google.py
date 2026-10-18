from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()

model = ChatGoogleGenerativeAI(model='gemini-3.8-flash',temperature=1.5)

result = model.invoke('give me count from starting from 1')

print(result.content[0]['text'])