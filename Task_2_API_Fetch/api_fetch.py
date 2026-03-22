import requests

API_URL = "https://jsonplaceholder.typicode.com/users"

def fetch_data():
    try:
        response = requests.get(API_URL)
        response.raise_for_status()  # Raises error if request fails
        return response.json()       # Parse JSON
    except requests.exceptions.RequestException as e:
        print("Error:", e)
        return []

def display_data(users):
    print("\n--- USER DATA ---\n")
    for user in users:
        print(f"Name : {user['name']}")
        print(f"Email: {user['email']}")
        print(f"City : {user['address']['city']}")
        print("-" * 30)

def search_data(users, keyword):
    return [
        user for user in users
        if keyword.lower() in user["name"].lower()
    ]

def main():
    users = fetch_data()

    if not users:
        return

    display_data(users)

    keyword = input("\nEnter name to search: ")

    results = search_data(users, keyword)

    print("\n--- SEARCH RESULTS ---\n")

    if results:
        display_data(results)
    else:
        print("No results found.")

if __name__ == "__main__":
    main()