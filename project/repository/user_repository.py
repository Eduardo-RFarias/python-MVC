from typing import Optional

from project.database.postgres_connector import PostgresConnector
from project.model.user import User


class UserRepository:
    def __init__(self):
        self.db = PostgresConnector()

    def findAll(self) -> list[User]:
        with self.db.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute("SELECT username, email, password, id FROM users")
                result = cursor.fetchall()

        users = [User(*row) for row in result]

        return users

    def findById(self, id: int) -> Optional[User]:
        with self.db.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT username, email, password, id FROM users WHERE id = %s", [id]
                )
                result = cursor.fetchone()

        if result is None:
            return None

        user = User(*result)

        return user

    def findByUsername(self, username: str) -> Optional[User]:
        with self.db.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "SELECT username, email, password, id FROM users WHERE username = %s",
                    [username],
                )
                result = cursor.fetchone()

        if result is None:
            return None

        user = User(*result)

        return user

    def save(self, user: User) -> None:
        with self.db.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "INSERT INTO users (username, email, password) VALUES (%s, %s, %s)",
                    [user.username, user.email, user.password],
                )

    def update(self, user: User) -> None:
        with self.db.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute(
                    "UPDATE users SET username = %s, email = %s, password = %s WHERE id = %s",
                    [user.username, user.email, user.password, user.id],
                )

    def delete(self, user: User) -> None:
        with self.db.connection as connection:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM users WHERE id = %s", [user.id])
