import requests

def get_random_quote():
    print("Fetching quote...... ")
    url = "http://api.quotable.io/random"
    response = requests.get(url)
    if response.status_code == 200:
        data = response.json()
        print(f"\n{data['content']}\n- {data['author']}\n")
    else:
        print("Failed to fetch quote.")

# Call the function
get_random_quote()


# print("Heloo bishalk")
    