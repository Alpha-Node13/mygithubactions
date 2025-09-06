import requests

# ❌ Hardcoded AWS secret 
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE"

# ❌ Hardcoded GitHub token 
GITHUB_TOKEN = "ghp_1234567890abcdefghijklmnopqrstuvwxyzABCDEFG"

# ❌ Hardcoded Stripe API key
STRIPE_API_KEY = "sk_test_51StripeKey1234567890"


def fetch_data():
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    response = requests.get("https://api.github.com/user", headers=headers)
    return response.json()


if __name__ == "__main__":
    print("⚠️ This is vulnerable code with fake secrets!")
    data = fetch_data()
    print(data)
