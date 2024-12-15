from flask import Flask, render_template, request, redirect, url_for, session
import pymysql

lucy = Flask(__name__)
lucy.secret_key = 'lucy0508'

# 데이터베이스 연결 설정
def get_db_connection():
    return pymysql.connect(
        host='localhost',
        user='songyaeji',
        password='syg03180320!',
        database='LucyDB',
        cursorclass=pymysql.cursors.DictCursor
    )

@lucy.route("/")
def start_func():
    return render_template('LucyWeb.html')

@lucy.route("/board", methods=["GET"])
def board_func():
    # 검색어 가져오기
    query = request.args.get('query', '').strip()
    
    connection = get_db_connection()
    try:
        with connection.cursor() as cursor:
            if query:
                # 검색어가 있을 경우 필터링
                sql = """
                    SELECT * FROM board
                    WHERE title LIKE %s OR content LIKE %s OR author LIKE %s
                """
                search_keyword = f"%{query}%"
                cursor.execute(sql, (search_keyword, search_keyword, search_keyword))
            else:
                # 검색어가 없을 경우 모든 데이터 가져오기
                sql = "SELECT * FROM board"
                cursor.execute(sql)
            results = cursor.fetchall()
    finally:
        connection.close()

    # HTML 렌더링, 검색어 포함
    return render_template('LucyBoard.html', board_data=results, query=query)

if __name__ == '__main__':
    lucy.debug = True
    lucy.run()