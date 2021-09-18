import sqlite3
from os import path

ROOT = path.dirname(path.realpath(__file__))


def criar_post(nome, sobrenome, email):
    conn = sqlite3.connect(path.join(ROOT, 'database.db'))
    cur = conn.cursor()
    cur.execute('insert into pessoas (nome, sobrenome, email) values (?, ?, ?)', (nome, sobrenome, email))
    conn.commit()
    conn.close()


def get_pessoas():
    conn = sqlite3.connect(path.join(ROOT, 'database.db'))
    cur = conn.cursor()
    cur.execute('select * from pessoas')
    pessoas = cur.fetchall()
    return pessoas
