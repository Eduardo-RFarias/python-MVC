from os import environ as env

DATABASE_URL = {
    "dbname": env.get("DB_NAME") or "sandbox",
    "user": env.get("DB_USER") or "postgres",
    "password": env.get("DB_PASSWORD") or "password",
    "host": env.get("DB_HOST") or "localhost",
    "port": env.get("DB_PORT") or "5432",
}
