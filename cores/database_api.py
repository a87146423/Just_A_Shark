import os

import psycopg2

DATABASE = os.environ.get("DATABASE_URL")

def init_database() -> None:
    conn = psycopg2.connect(DATABASE, sslmode='require')
    cursor = conn.cursor()
    try:
        sql = "CREATE TABLE TempVoices (server_id BIGINT, temp_channel_id BIGINT, temp_text_channel BOOLEAN)"
        cursor.execute(sql)
        conn.commit()
    except:
        pass

    cursor.close()
    conn.close()

def add_temp_voices(server_id: int, channel_id: int) -> None:
    conn = psycopg2.connect(DATABASE, sslmode='require')
    cursor = conn.cursor()
    sql = f"INSERT INTO TempVoices VALUES({int(server_id)}, {int(channel_id)}, FALSE)"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def set_temp_voices(server_id: int, channel_id: int, toggle_text: bool) -> None:
    conn = psycopg2.connect(DATABASE, sslmode='require')
    cursor = conn.cursor()
    sql = f"UPDATE TempVoices SET temp_channel_id = {int(channel_id)}, temp_text_channel = {bool(toggle_text)} WHERE server_id = {int(server_id)}"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()

def remove_temp_voices(server_id: int) -> None:
    conn = psycopg2.connect(DATABASE, sslmode='require')
    cursor = conn.cursor()
    sql = f"DELETE FROM TempVoices WHERE server_id = {int(server_id)}"
    cursor.execute(sql)
    conn.commit()
    cursor.close()
    conn.close()
