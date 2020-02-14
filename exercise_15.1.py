import sqlite3

conn = sqlite3.connect('music.sqlite')
cur = conn.cursor()

cur.executescript('''
DROP TABLE IF EXISTS Ages;
CREATE TABLE Ages (name VARCHAR(128), age INTEGER);
DELETE FROM Ages;
INSERT INTO Ages (name, age) VALUES ('Armen', 38);
INSERT INTO Ages (name, age) VALUES ('Qasim', 17);
INSERT INTO Ages (name, age) VALUES ('Martin', 32);
INSERT INTO Ages (name, age) VALUES ('Bekim', 18);
''')

cur.execute('SELECT hex(name || age) AS X FROM Ages ORDER BY X')
for row in cur:
     print(row)
