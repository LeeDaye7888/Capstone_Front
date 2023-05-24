from flask import Flask, render_template, url_for, session, request, redirect
import sys
import mysql.connector
import json

mydb = mysql.connector.connect(
    host="localhost",
    user="test",
    password="test",        #비밀번호
    user="",
    password="",  # 비밀번호
)
mycursor = mydb.cursor()
mycursor.execute("USE testdb")


# 커뮤니티_글목록
def community_list():

    sql = "SELECT * FROM community"

    mycursor.execute(sql)
    row = mycursor.fetchall()

    result = []
    if len(row) > 0:
        for i in range(len(row)):
            data = {
                'serial_number': row[i][0],
                'id': row[i][1],
                'title': row[i][2]
            }
            result.append(data)
        community_list_json = json.dumps(result)

    else:
        print("No data found.")

    return community_list_json
