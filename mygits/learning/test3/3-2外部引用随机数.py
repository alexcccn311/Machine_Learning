import requests
response = requests.get("https://www.random.org/integers/?num=1&min=1&max=100&col=1&base=10&format=plain&rnd=new")
true_random_number = int(response.text.strip())

print(true_random_number)