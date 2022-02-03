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
        # ユーザーから入力された値を変数「command」に定義。
        command = input('Your command > ')
        # ユーザーから入力された値を大文字にして変数「command_upper」に定義。
        command_upper = command.upper()

        if command_upper == 'S':
            # 関数「all_users()」に格納されている値を取り出し、繰り返し情報を入れていく。
            users = all_users()
            for user in users:
                print(f"Name: {user[0]} | Age: {user[1]}")

        elif command_upper == 'A':
            # ユーザーから入力された名前情報を変数「name」に定義。
            name = input('New user name > ')
            # ユーザーから入力された名前情報を変数「age」に定義。
            age = input('New user age > ')
            print(f"Add new user: {name}")
            # 関数「register」に引数として「name」「age」を渡す。
            register_user(name, age)

        elif command_upper == 'Q':
            print("Bye!")
            # 終わらせる。
            break

        else:
            # 小文字で入力されたら小文字で返してほしいので、大文字にする前のそのままの値「command」を使用する。
            print(f"{command}: command not found")


if __name__ == '__main__':
    main()
    