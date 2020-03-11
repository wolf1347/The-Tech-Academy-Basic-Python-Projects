import sqlite3

conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("CREATE TABLE IF NOT EXISTS tbl_files( \
        ID INTEGER PRIMARY KEY AUTOINCREMENT, \
        col_fileList VARCHAR(50) \
        )")
    conn.commit()
conn.close()

fileList = ['information.docx','Hello.txt','myImage.png', \
            'myMovie.mpg','World.txt','data.pdf','myPhoto.jpg']

int i = 0
for fileName in fileList:
    if fileName.find("txt") != -1:
        print (fileName)
        cur.execute("INSERT INTO tbl_files(col_fileList) VALUES (?)", \
                (fileList[i],))
        i++
        
conn = sqlite3.connect('drill.db')

with conn:
    cur = conn.cursor()
    cur.execute("INSERT INTO tbl_files(col_fileList) VALUES (?)", \
                (fileList[1],))
    cur.execute("INSERT INTO tbl_files(col_fileList) VALUES (?)", \
                (fileList[4],))
    conn.commit()
conn.close()



        
