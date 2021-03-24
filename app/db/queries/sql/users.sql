-- name: create-user^
INSERT INTO users
(user_name, full_name, email, hashed_password, created_at)
VALUES (
    :user_name,
    :full_name,
    :email,
    crypt(
        :password,
        gen_salt('bf', 8)
    ),
    now()
)RETURNING id, user_name, full_name;

--name: get-user^
SELECT id, user_name, full_name
FROM users
WHERE
    user_name = :user_name
    AND
    hashed_password = crypt(
        :password,
        hashed_password
    );