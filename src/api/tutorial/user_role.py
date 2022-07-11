import json
import os.path


class Role:
    def __init__(self):
        with open(os.path.join(os.getenv("SECRETE"), "tutorial_reddit_role.json")) as file:
            self.role = json.load(file)
        self.USER = self.role.get("user")
        self.TESTER = self.role.get("tester")
        self.MODERATOR = self.role.get("moderator")
        self.VIP = self.role.get("vip")
        self.ADMIN = self.role.get("ADMIN")

    def get_role(self, role: str):
        role_int = self.role.get(role)
        if role_int:
            return role_int