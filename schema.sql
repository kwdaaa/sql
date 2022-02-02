--もしusersテーブルが存在したら消しますよ。
DROP TABLE IF EXISTS users;

--もしusersテーブルがあったら作らないでね。
CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    age INTEGER
);

--初期データを入れる。
INSERT INTO users
VALUES
    ('Bob', 15),
    ('Tom', 57),
    ('Ken', 73)
;