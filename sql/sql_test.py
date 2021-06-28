import sqlite3

con = sqlite3.connect('pbl.db')
cur = con.cursor()

cur.execute('''
    insert into teammate values(4, 'none', '192.168.100.234')
''')

# print('ok')

con.commit()
con.close()
