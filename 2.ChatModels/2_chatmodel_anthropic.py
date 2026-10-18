from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv() # there is no api key in .env file

model = ChatAnthropic(model='claude-3-5-sonnet-20241022')

result = model.invoke('What is the capital of India')

print(result.content)