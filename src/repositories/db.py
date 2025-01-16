class FakeDatabaseHandler:
    def __init__(self):
        self.users = users = [
            {
                "user_id": i,
                "username": f"user_{i}",
                "addresses": [],
                "is_active": bool(i % 7 != 0),
            }
            for i in range(100000)
        ]
        self.products = [
            {"product_id": i, "name": f"product_{i}", "price": i * 100}
            for i in range(100)
        ]

    def get_all_users(
        self, include_inactive: bool = False, limit: int = 10, offset: int = 0
    ):
        users = (
            list(filter(lambda x: x["is_active"] == True, self.users))
            if not include_inactive
            else self.users
        )
        return users[offset: limit + offset:]

    def get_user(self, user_id: int):
        try:
            return list(filter(lambda x: x["user_id"] == user_id, self.users))[0]
        except IndexError:
            return None

    def create_user(self, payload: dict):
        username = payload["username"]
        for u in self.users:
            if u["username"] == username:
                return False
        last_user = self.users[-1]
        last_id = last_user["user_id"]
        self.users.append(
            {"user_id": last_id + 1, "username": username,
                "is_active": True, "addresses": []}
        )
        return self.users[-1]

    def inactivate_user(self, user_id: int):
        for user in self.users:
            if user["user_id"] == user_id:
                user["is_active"] = False
                return

    def get_user_adresses(self, user_id: int):
        user = self.get_user(user_id)
        return user.get("addresses", [])

    def add_user_address(self, user_id: int, address: str):
        user = self.get_user(user_id)
        user.get("addresses", []).append(address)
        return
