-- name: create-file^
INSERT INTO files (file_path, user_name, created_at)
VALUES (
    :file_path,
    :user_name,
    now()
);