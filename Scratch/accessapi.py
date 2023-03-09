import openai

secret_key = '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'
prompt = 'Tell me a slog for a home security company'
tokens = 200
openai.api_key = secret_key

output = openai.Completion.create(
    model = 'text-davinci-003',
    prompt = prompt,
    max_tokens = tokens,
    temperature = 0
)

output_text = output['choices'][0]['text']

print(output_text)