import unittest
import requests
from datetime import datetime
import random

# === CONFIG: Replace these ===
BASE_URL = "https://mental-health-backend-production.up.railway.app"
USER_ID_TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjkwOTg1NzhjNDg4MWRjMDVlYmYxOWExNWJhMjJkOGZkMWFiMzRjOGEiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoidGlubyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9tZW50YWxoZWFsdGhjaGF0Ym90LWRkMGJiIiwiYXVkIjoibWVudGFsaGVhbHRoY2hhdGJvdC1kZDBiYiIsImF1dGhfdGltZSI6MTc0NTQ0ODQ4OCwidXNlcl9pZCI6ImdWSGJXaXAxQmdZRUtwT0pOWk5Tb0NZdHJ2eDIiLCJzdWIiOiJnVkhiV2lwMUJnWUVLcE9KTlpOU29DWXRydngyIiwiaWF0IjoxNzQ1NDQ4NDg5LCJleHAiOjE3NDU0NTIwODksImVtYWlsIjoidGlub0BhbGlhcy5sb2NhbCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJ0aW5vQGFsaWFzLmxvY2FsIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.Hne9LMJojEeKnlfKnqcsRRNMScaaJ1IazQ9bPoZfi4LZoJfR6v2m-B2SWTlk1Fj-ydTruseeBwARsdCVtbM4HDBdBv8VWFFcpFMg3_daEKrqgw9hZuSm2iFK5ArMSGYujwYJS7JBnt5mNTUcPShNpTPNe5gs-lJMaDqS7dpkU7s3j-b_MxoGYJhsdioqZWp0dAiFAA5YjZDzDIRB6mORYNyjG8PbcJwyUTECNdKJOZTkRQhHoMkUsTT-eeq_NEdUTewLCctC61lw7zumOZvO9-CfCHBEfy3M9ktbCobEJ6ZXMZNfM8vbNk_ofZG2GmfmQctHdTnz9k7IoxeuNtT9ig"
ADMIN_ID_TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjkwOTg1NzhjNDg4MWRjMDVlYmYxOWExNWJhMjJkOGZkMWFiMzRjOGEiLCJ0eXAiOiJKV1QifQ.eyJhZG1pbiI6dHJ1ZSwiaXNzIjoiaHR0cHM6Ly9zZWN1cmV0b2tlbi5nb29nbGUuY29tL21lbnRhbGhlYWx0aGNoYXRib3QtZGQwYmIiLCJhdWQiOiJtZW50YWxoZWFsdGhjaGF0Ym90LWRkMGJiIiwiYXV0aF90aW1lIjoxNzQ1NDQ4NjU3LCJ1c2VyX2lkIjoiS2wydjlPNGlsZlFjNUZCZGxFb2o1a2l6YTlzMSIsInN1YiI6IktsMnY5TzRpbGZRYzVGQmRsRW9qNWtpemE5czEiLCJpYXQiOjE3NDU0NDg2NTcsImV4cCI6MTc0NTQ1MjI1NywiZW1haWwiOiJhZG1pbkBhbGlhcy5sb2NhbCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJhZG1pbkBhbGlhcy5sb2NhbCJdfSwic2lnbl9pbl9wcm92aWRlciI6InBhc3N3b3JkIn19.V8VRMXM9f4Mm5nSzxmm_oRuVw_novyZ92JdWf_1M1cmReXvOrsUlENjLKudrUC-RKcc13jA8Z-rYv_BjJtJvrXfuuRQFsC5dhoINHJxhI1beyJoHukdGpS3Vpw3KKKqnJV5rEzc1uT9gREHD0GPsJYe5Pk13ijdiq1qUMOvj6-181aqqPSZKoAL3g1k_TRgGsvyfmAk22vU69dbIDn4PWm-hN0pT2u3QjozlMWmLCZn3tTk3cM6FVqo_3lt7eMghFRhTMJlayOeWakNwD2iPgM6Ff2ZEM26DbHgcL3n6NMD6HDOn5Ys1Y9Q-U8q8xDC6H1igLbvZvDEesdOcxHR0Eg"
USER_UID = "TNLNximdMQNylvnufaRL7zkUbsg1"


headers_user = {"Authorization": f"Bearer {USER_ID_TOKEN}"}
headers_admin = {"Authorization": f"Bearer {ADMIN_ID_TOKEN}"}

class TestMentalHealthBackend(unittest.TestCase):

    def test_1_save_preferences(self):
        res = requests.post(f"{BASE_URL}/save-preferences", headers=headers_user, json={
            "user_id": USER_UID,
            "preferences": {"theme": "light"}
        })
        self.assertEqual(res.status_code, 200)

    def test_2_get_preferences(self):
        res = requests.get(f"{BASE_URL}/get-preferences", headers=headers_user, params={
            "user_id": USER_UID
        })
        self.assertEqual(res.status_code, 200)

    def test_3_submit_feedback(self):
        res = requests.post(f"{BASE_URL}/feedback", headers=headers_user, json={
            "user_id": USER_UID,
            "rating": random.randint(1, 5),
            "comment": "Automated test feedback",
            "timestamp": datetime.utcnow().isoformat()
        })
        self.assertEqual(res.status_code, 201)

    def test_4_get_feedback_as_admin(self):
        res = requests.get(f"{BASE_URL}/feedback", headers=headers_admin)
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.json(), list)

    def test_5_get_feedback_as_user_forbidden(self):
        res = requests.get(f"{BASE_URL}/feedback", headers=headers_user)
        self.assertEqual(res.status_code, 403)

    def test_6_submit_mood(self):
        res = requests.post(f"{BASE_URL}/mood", headers=headers_user, json={
            "user_id": USER_UID,
            "mood": "happy",
            "timestamp": datetime.utcnow().isoformat()
        })
        self.assertEqual(res.status_code, 201)

    def test_7_get_mood_entries(self):
        res = requests.get(f"{BASE_URL}/mood", headers=headers_user, params={
            "user_id": USER_UID
        })
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.json(), list)

    def test_8_submit_journal(self):
        res = requests.post(f"{BASE_URL}/journal", headers=headers_user, json={
            "user_id": USER_UID,
            "text": "Automated test journal entry",
            "timestamp": datetime.utcnow().isoformat()
        })
        self.assertEqual(res.status_code, 201)

    def test_9_get_journal_entries(self):
        res = requests.get(f"{BASE_URL}/journal", headers=headers_user, params={
            "user_id": USER_UID
        })
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.json(), list)

    def test_10_submit_assessment(self):
        res = requests.post(f"{BASE_URL}/assessment", headers=headers_user, json={
            "user_id": USER_UID,
            "score": {"phq9": 10, "gad7": 7},
            "responses": {"q1": 2, "q2": 1}
        })
        self.assertEqual(res.status_code, 201)

    def test_11_get_assessments(self):
        res = requests.get(f"{BASE_URL}/assessment/results", headers=headers_user, params={
            "user_id": USER_UID
        })
        self.assertEqual(res.status_code, 200)
        self.assertIsInstance(res.json(), list)

    def test_12_chat_submit_and_history(self):
        session_id = datetime.now().strftime("test-%H%M%S")
        message = f"Hello bot at {datetime.now().isoformat()}"

        # Send message
        send = requests.post(f"{BASE_URL}/chat", headers=headers_user, json={
            "user_id": USER_UID,
            "message": message,
            "session_id": session_id
        })
        self.assertEqual(send.status_code, 200)

        # Get history
        hist = requests.get(f"{BASE_URL}/chat-history", headers=headers_user, params={
            "user_id": USER_UID,
            "session_id": session_id
        })
        self.assertEqual(hist.status_code, 200)
        self.assertIn("messages", hist.json())

    def test_13_chat_sessions_list(self):
        res = requests.get(f"{BASE_URL}/chat-sessions", headers=headers_user, params={
            "user_id": USER_UID
        })
        self.assertEqual(res.status_code, 200)
        self.assertIn("sessions", res.json())


if __name__ == "__main__":
    unittest.main()