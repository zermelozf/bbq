import requests

def get_quote():
  url = 'https://breaking-bad-quotes.herokuapp.com/v1/quotes'
  res = requests.get(url).json()[0]
  return f"{res['author']} said \"{res['quote']}\""

if __name__ == "__main__":
  print(get_quote())