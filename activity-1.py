import os 
import openai

os.environ['API_KEY'] = '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'
openai.api_key = os.environ.get('API_KEY')

response = openai.completions.create(
    model = "text-davinci-002",
    prompt = "Once upon a time, when the world was young,",
    max_tokens = 75
)

print(response.choices)