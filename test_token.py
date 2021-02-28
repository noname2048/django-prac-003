import requests

JWT_TOKEN = (
    "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9."
    "eyJ1c2VyX2lkIjoyLCJ1c2VybmFtZSI6InVzZXIyIiwi"
    "ZXhwIjoxNjEzOTEyMzM1LCJlbWFpbCI6IiIsIm9yaWdfaWF0I"
    "joxNjEzOTEyMDM1fQ.MVpC_99s5YTMWC6G_CHgsigIlqFoUfbZ45ovEAnXZgI"
)

headers = {
    "Authorization": f"JWT {JWT_TOKEN}",
}

res = requests.get("localhost:8000/posts/1/", headers=headers)
