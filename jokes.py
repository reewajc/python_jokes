import pyjokes

# joke = pyjokes.get_joke(language='en')
# print(joke)

jokes = pyjokes.get_jokes(language='en')

for joke in jokes:
    print(joke)