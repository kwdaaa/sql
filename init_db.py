import os

from dotenv import load_dotenv

import psycopg2

load_dotenv()


# データベースの初期化
def init_db():
    # ●DBの情報を取得
    dsn = os.environ.get('DATABASE_URL')

    # DBに接続（コネクションを貼る）
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()

    # ●SQLを用意
    # ●SQLを実行
    # テーブルとレコードを用意（型も指定して）
    with open('schema.sql', encoding="utf-8") as f:
        sql = f.read()
        cur.execute(sql)

    # ●実行状態を保存
    conn.commit()

    # ●コネクションを閉じる
    conn.close()


# 全てのユーザーの情報を取得（command 'S'）
def all_users():
    # ●DBの情報を取得
    dsn = os.environ.get('DATABASE_URL')

    # DBに接続（コネクションを貼る）
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()
    # すべてのユーザー情報を取得
    sql = "SELECT * FROM users;"
    cur.execute(sql)
    # 関数「users」に全部読み込んだデータを入れる。
    users = cur.fetchall()
    conn.commit()
    conn.close()

    return users


# 2回目以降データを登録（command 'A'）
def register_user(name, age):
    # ●DBの情報を取得
    dsn = os.environ.get('DATABASE_URL')

    # DBに接続（コネクションを貼る）
    conn = psycopg2.connect(dsn)
    cur = conn.cursor()

    # ●SQLを用意
    # データを入れる。
    # 「INSERT　INTO」はデータを投入する命令。usersというテーブルのnameとageのカラムに対して、{name}と{age}の値を入れます。
    sql = "INSERT INTO users (name, age) VALUES (%(name)s, %(age)s)"

    # ●SQLを実行
    cur.execute(sql, {'name': name, 'age': age})

    # ●実行状態を保存
    conn.commit()

    # ●コネクションを閉じる
    conn.close()


def main():
    # データベースの初期化
    init_db()

    welcome_message = "===== Welcome to CRM Application =====\n" \
                      "[S]how: Show all users info\n" \
                      "[A]dd: Add new user\n" \
                      "[Q]uit: Quit The Application\n" \
                      "======================================"
    print(welcome_message)

    # 繰り返し
    while True:
        print()
        command = input('Your command > ').upper()
        if command == 'S':
            users = all_users()
            for user in users:
                print(f"Name: {user[0]} | Age: {user[1]}")

        elif command == 'A':
            name = input('New user name > ')
            age = input('New user age > ')
            print(f"Add new user: {name}")
            register_user(name, age)

        elif command == 'Q':
            print("Bye!")
            break

        else:
            print(f"{command}: command not found")


if __name__ == '__main__':
    main()
    