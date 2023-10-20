import os 
import openai

os.environ['API_KEY'] = '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'
openai.api_key = os.environ.get('API_KEY')

prompt = "What are the public hours for the bank's city branch?"

response = openai.completions.create(
    model = "text-davinci-003",
    prompt = prompt,
    max_tokens = 75,
)

print("Model: ", response.model)
print("Created: ", response.created)
print("ID: ", response.id)

response_print = response.choices[0].text.strip()
print(response_print)
