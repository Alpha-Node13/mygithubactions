import requests

# ❌ Hardcoded AWS secret 
AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLE123"

# ❌ Hardcoded GitHub token 
GITHUB_TOKEN = "ghp_abCDefGhijkLmnoPQRStuvWxyz1234567890"

# ❌ Hardcoded Stripe API key
STRIPE_API_KEY = "sk_test_4eC39HqLyjWDarjtT1zdp7dc"


def fetch_data():
    headers = {"Authorization": f"Bearer {GITHUB_TOKEN}"}
    response = requests.get("https://api.github.com/user", headers=headers)
    return response.json()


if __name__ == "__main__":
    print("⚠️ This is vulnerable code with fake secrets!")
    data = fetch_data()
    print(data)
