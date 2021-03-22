-- name: create-user^
INSERT INTO users
(username, fullname, email, hashed_password, created_at)
VALUES (
    :username,
    :fullname,
    :email,
    crypt(
        :password,
        gen_salt('bf', 8)
    ),
    now()
)RETURNING id, username, fullname;

--name: get-user-id^
SELECT id, username, fullname
FROM users
WHERE
    login = :login
    AND
    hashed_password = crypt(
        :password,
        hashed_password
    );