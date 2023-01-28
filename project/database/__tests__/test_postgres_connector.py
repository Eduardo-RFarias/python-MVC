import unittest


class PostgresConnectorTests(unittest.TestCase):
    def test_connect(self):
        # Arrange
        from project.database.postgres_connector import PostgresConnector

        # Act
        postgres_connector = PostgresConnector()

        # Assert
        self.assertIsNotNone(postgres_connector.connection)

        with postgres_connector.connection.cursor() as cursor:
            cursor.execute("SELECT 1")
            result = cursor.fetchone()

        self.assertEqual(result, (1,))
