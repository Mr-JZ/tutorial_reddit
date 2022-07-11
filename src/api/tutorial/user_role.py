import json
import os.path


class Role:
    def __init__(self):
        self.role = json.loads(os.getenv("TUTORIAL_REDDIT_ROLE"))
        self.USER = self.role.get("user")
        self.TESTER = self.role.get("tester")
        self.MODERATOR = self.role.get("moderator")
        self.VIP = self.role.get("vip")
        self.ADMIN = self.role.get("ADMIN")

    def get_role(self, role: str):
        role_int = self.role.get(role)
        if role_int:
            return role_int