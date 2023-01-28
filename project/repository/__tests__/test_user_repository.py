import unittest

import psycopg2

from project.database.postgres_connector import PostgresConnector
from project.model.user import User
from project.repository.user_repository import UserRepository


class UserRepositoryTests(unittest.TestCase):
    user_repository = UserRepository()

    def tearDown(self):
        with PostgresConnector().connection as connection:
            with connection.cursor() as cursor:
                cursor.execute("DELETE FROM users;")

    def test_create_user__with_valid_data__expect_success(self):
        # Arrange
        user_to_create = User("John Doe", "example@email.com", "password")

        # Act
        self.user_repository.save(user_to_create)
        user = self.user_repository.findByUsername(user_to_create.username)

        # Assert
        self.assertIsNotNone(user)

    def test_create_user__with_duplicate_username__expect_to_fail(self):
        # Arrange
        user_to_create = User("John Doe", "example@email.com", "password")

        # Act and Assert
        self.user_repository.save(user_to_create)

        with self.assertRaises(psycopg2.IntegrityError):
            self.user_repository.save(user_to_create)

    def test_get_all_users__with_two_users__returns_two_users(self):
        # Arrange
        users = [
            User("John", "example@email.com", "password"),
            User("Mary", "example@email.com", "password"),
        ]

        for user in users:
            self.user_repository.save(user)

        # Act
        users_retrieved = self.user_repository.findAll()

        # Assert
        self.assertEqual(len(users_retrieved), 2)

    def test_get_user_by_id__with_existing_user__returns_user(self):
        # Arrange
        user_to_create = User("Mary Doe", "example@email.com", "password")
        self.user_repository.save(user_to_create)
        saved_id = self.user_repository.findByUsername(user_to_create.username).id

        # Act
        user = self.user_repository.findById(saved_id)

        # Assert
        self.assertIsNotNone(user)

    def test_get_user_by_id__with_non_existing_user__returns_none(self):
        # Arrange and Act
        user = self.user_repository.findById(1)

        # Assert
        self.assertIsNone(user)

    def test_get_user_by_username__with_existing_user__returns_user(self):
        # Arrange
        user_to_create = User("Mary Doe", "example@email.com", "password")
        self.user_repository.save(user_to_create)

        # Act
        user = self.user_repository.findByUsername(user_to_create.username)

        # Assert
        self.assertIsNotNone(user)
        self.assertEqual(user.username, user_to_create.username)

    def test_get_user_by_username__with_non_existing_user__returns_none(self):
        # Arrange and Act
        user = self.user_repository.findByUsername("John Doe")

        # Assert
        self.assertIsNone(user)

    def test_update_user__with_existing_user__expect_success(self):
        # Arrange
        user_to_create = User("John Doe", "example@email.com", "password")
        self.user_repository.save(user_to_create)
        saved_user = self.user_repository.findByUsername(user_to_create.username)

        saved_user.username = "Mary Doe"

        # Act
        self.user_repository.update(saved_user)

        # Assert
        updated_user = self.user_repository.findById(saved_user.id)
        self.assertEqual(updated_user.username, saved_user.username)

    def test_delete_user__with_existing_user__expect_success(self):
        # Arrange
        user_to_create = User("John Doe", "example@email.com", "password")
        self.user_repository.save(user_to_create)
        saved_user = self.user_repository.findByUsername(user_to_create.username)

        # Act
        self.user_repository.delete(saved_user)

        # Assert
        deleted_user = self.user_repository.findById(saved_user.id)
        self.assertIsNone(deleted_user)
