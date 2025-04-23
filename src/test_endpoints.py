import unittest
import requests
from datetime import datetime
import random

# === CONFIG: Replace these ===
BASE_URL = "http://localhost:5000"
USER_ID_TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjkwOTg1NzhjNDg4MWRjMDVlYmYxOWExNWJhMjJkOGZkMWFiMzRjOGEiLCJ0eXAiOiJKV1QifQ.eyJuYW1lIjoidGlubyIsImlzcyI6Imh0dHBzOi8vc2VjdXJldG9rZW4uZ29vZ2xlLmNvbS9tZW50YWxoZWFsdGhjaGF0Ym90LWRkMGJiIiwiYXVkIjoibWVudGFsaGVhbHRoY2hhdGJvdC1kZDBiYiIsImF1dGhfdGltZSI6MTc0NTM2MTk1MywidXNlcl9pZCI6IlROTE54aW1kTVFOeWx2bnVmYVJMN3prVWJzZzEiLCJzdWIiOiJUTkxOeGltZE1RTnlsdm51ZmFSTDd6a1Vic2cxIiwiaWF0IjoxNzQ1MzYxOTUzLCJleHAiOjE3NDUzNjU1NTMsImVtYWlsIjoidGlub0BhbGlhcy5sb2NhbCIsImVtYWlsX3ZlcmlmaWVkIjpmYWxzZSwiZmlyZWJhc2UiOnsiaWRlbnRpdGllcyI6eyJlbWFpbCI6WyJ0aW5vQGFsaWFzLmxvY2FsIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.T8bmokCYYVRtmcCdSWlwzOHwQiN3NX8yOoGcPdiTVJH0qpaCD7A4d0EhutTnGgsl0TvaFGKpTbq9J0iG4wCv5C9otAMWzZ_CKQbQK3n9eJUipzPRN8qpJhjfkR9XJlB2jHuiAgeUfFkpqeK_vksdgSIkAh83sMKxByNOtzlqYo8QYTPPLVcQUxFdUBJ1qXQ0u_Vqo2BPrYZXZOfmsKO3Y66sDId5vV97ArEXkvTWGwVo8KYyIBn5DTbVqyBvyex5m1LD86UyVpJwhNN8ULOVowkyGCqnar6N5pZbs6YQXQ9ZbLd-m505xFwGWIpTyWSgRrmlTCruiCY05Fd8Dy2y4Q"
ADMIN_ID_TOKEN = "eyJhbGciOiJSUzI1NiIsImtpZCI6IjkwOTg1NzhjNDg4MWRjMDVlYmYxOWExNWJhMjJkOGZkMWFiMzRjOGEiLCJ0eXAiOiJKV1QifQ.eyJpc3MiOiJodHRwczovL3NlY3VyZXRva2VuLmdvb2dsZS5jb20vbWVudGFsaGVhbHRoY2hhdGJvdC1kZDBiYiIsImF1ZCI6Im1lbnRhbGhlYWx0aGNoYXRib3QtZGQwYmIiLCJhdXRoX3RpbWUiOjE3NDUzNjIwMTksInVzZXJfaWQiOiJLbDJ2OU80aWxmUWM1RkJkbEVvajVraXphOXMxIiwic3ViIjoiS2wydjlPNGlsZlFjNUZCZGxFb2o1a2l6YTlzMSIsImlhdCI6MTc0NTM2MjAxOSwiZXhwIjoxNzQ1MzY1NjE5LCJlbWFpbCI6ImFkbWluQGFsaWFzLmxvY2FsIiwiZW1haWxfdmVyaWZpZWQiOmZhbHNlLCJmaXJlYmFzZSI6eyJpZGVudGl0aWVzIjp7ImVtYWlsIjpbImFkbWluQGFsaWFzLmxvY2FsIl19LCJzaWduX2luX3Byb3ZpZGVyIjoicGFzc3dvcmQifX0.cZ2yWy9xmDGaT4Gfx9yYi8C_PCcqi9CJJl4_a8m4DhT3h3WwYx-tIsazP9Xd0eJ-UgEW-B06RsbgsGCcgrOror7sgqv-D7Jbp8IeHVc9wO-566d3fLCgS4F8g2fhaY4rRtteKTxU1wW-PqCLHo9iCd8QOYzuk3MP1rksO4_osy7RwEuTAW5taY3VLXjX7fpqTAQvQo71hYl_HhmBJWt-2F5mUHtn-BOaCut-J7CRptVsv7lTCnGEiNJVf42EJUBPI3qH_ckY4pZfpVctYDz_zpgALGnNuELNBYpakQiEnCqmNLKJw-Bh3FVBoIf9H20dn-oQBKXlePCL_ASXrr15ow"
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