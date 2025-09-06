import requests

# ❌ Hardcoded AWS secret (FAKE example)
AWS_SECRET_KEY = ""

# ❌ Hardcoded GitHub token (FAKE example)
GITHUB_TOKEN = ""

# ❌ Hardcoded Stripe API key (FAKE example)
STRIPE_API_KEY = ""


def fetch_data():
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    response = requests.get("https://api.github.com/user", headers=headers)
    return response.json()


if __name__ == "__main__":
    print("⚠️ This is vulnerable code with fake secrets!")
    data = fetch_data()
    print(data)
