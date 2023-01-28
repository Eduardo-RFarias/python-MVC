CREATE TABLE "users" (
    "id" SERIAL NOT NULL,
    "username" VARCHAR(50) NOT NULL,
    "password" VARCHAR(100) NOT NULL,
    "email" VARCHAR(100) NOT NULL,
    CONSTRAINT "user_pk" PRIMARY KEY ("id"),
    CONSTRAINT "user_username_uk" UNIQUE ("username")
);