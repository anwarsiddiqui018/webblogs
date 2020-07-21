# Import libraries
import pandas as pd, csv, sqlite3
database = r"C:\SimplyAli\Django\Django2__updated__\db.sqlite3"
# Create sqlite database and cursor
conn = sqlite3.connect(database)
c = conn.cursor()
# Create the table of pitches
c.execute("""CREATE TABLE IF NOT EXISTS pitches (
            pitch_type text,
            game_date text,
            release_speed real
            )""")
conn.commit()

test = conn.execute('SELECT * from pitches')
names = [description[0] for description in test.description]
print(names)

df = pd.DataFrame([['SL','8/31/2017','81.9']],columns = ['pitch_type','game_date','release_speed'])
df.to_sql('pitches', conn, if_exists='append', index=False)

conn.execute('SELECT * from pitches').fetchall()
