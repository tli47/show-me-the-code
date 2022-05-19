__author__ = 'tli47'

import random, string
import MySQLdb

ALL_LETTERS = string.ascii_lowercase + string.digits
codeAmount = 200
codeRound = 10
codeResult = []

while len(codeResult) != codeAmount:
    everyCode = ''.join((random.choice(ALL_LETTERS) for i in range(codeRound)))
    if everyCode not in codeResult:
        codeResult.append(everyCode)

conn = MySQLdb.connect('localhost', 'root', '123456', 'test', charset='utf8')
cursor = conn.cursor()

sql = 'create table if not exists mykeys (key_id char(36) not null)'
cursor.execute(sql)


for key in codeResult:
    cursor.execute("insert into mykeys values ('%s')" % str(key))

cursor.close()
conn.commit()
conn.close()