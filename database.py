import sqlite3


def add_user(email,password):
    worth = 10000
    conn = sqlite3.connect('member.db')
    c = conn.cursor()
    c.execute("INSERT INTO members VALUES(?,?,?)",(email,password,worth))
    conn.commit()
    conn.close()
#returns true if a member exist.
def find_user(email,password):
    flag = False
    conn = sqlite3.connect('member.db')
    c = conn.cursor()
    c.execute("SELECT * FROM members WHERE email='{}' and user_password='{}' ".format(email,password))
    for i in c.fetchall():
        if i:
            flag = True
    conn.commit()
    conn.close()
    return flag

def is_valid_mail(email):
    conn = sqlite3.connect('member.db')
    c = conn.cursor()
    c.execute("SELECT * FROM members")
    users = c.fetchall()
    for user in users:
        for mail in user:
            if mail==email:
                return False
    conn.commit()
    conn.close()
    return True


def add_stock(email,stock_name,piece,price):
    conn = sqlite3.connect('member.db')
    cursor = conn.cursor()
    cursor.execute(" SELECT * FROM STOCKS WHERE email='{}'".format(email))
    user = cursor.fetchall()

    #aynı hisseden içerde var ise bir güncelleme yapar.
    for i in user:
        if email in i and stock_name in i:

            cursor.execute(" SELECT * FROM members WHERE email='{}'".format(email))
            usr = cursor.fetchall()

            for k in usr:
                new_worth = k[2]-piece*price

            if new_worth>=0:
                cursor.execute(" UPDATE members SET worth='{}' WHERE email='{}'".format(new_worth,email)) 
                conn.commit()

                new_piece = i[2]+piece

                cursor.execute(" UPDATE STOCKS SET stock_piece='{}' WHERE stock_name='{}'".format(new_piece,stock_name))
                conn.commit()
                conn.close()
                return

    cursor.execute(" SELECT * FROM members WHERE email='{}'".format(email))
    usr = cursor.fetchall()
    for k in usr:
        new_worth = k[2]-piece*price

        if new_worth>=0:
            cursor.execute(" UPDATE members SET worth='{}' WHERE email='{}'".format(new_worth,email)) 
            conn.commit()
            cursor.execute("INSERT INTO STOCKS VALUES(?,?,?)",(email,stock_name,piece))
            conn.commit()

    conn.close()



def remove_stock(email,stock_name,stock_piece,price):
    conn = sqlite3.connect('member.db')
    c = conn.cursor()
    c.execute("SELECT * FROM STOCKS")
    users = c.fetchall()
    for i in users:
        if email in i and stock_name in i and stock_piece<=i[2]:
            c.execute(" SELECT * FROM members WHERE email='{}'".format(email))
            user = c.fetchall()
            piece = i[2]-stock_piece
            for k in user:
                new_worth = stock_piece*price+k[2]
            conn.commit()
            c.execute(" UPDATE members SET worth='{}' WHERE email='{}'".format(new_worth,email))
            conn.commit()
            #burada elindeki hisselerin sadece bir kısmını satmak isteyenler için bir update oluştur.
            
            if piece==0:
                c.execute("DELETE FROM STOCKS WHERE email='{}' and stock_name='{}' and stock_piece='{}' ".format(email,stock_name,stock_piece))
                conn.commit()
            else:
                c.execute(" UPDATE STOCKS SET stock_piece='{}' WHERE stock_name='{}'".format(piece,stock_name))
                conn.commit()

    conn.commit()
    conn.close()


def learn_budget(email):
    conn = sqlite3.connect('member.db')
    c = conn.cursor()
    c.execute("SELECT * FROM members WHERE email='{}'".format(email))
    user = c.fetchall()
    conn.commit()
    conn.close()
    for i in user:
        return i[2]

def learn_stocks_and_piece(email):
    conn = sqlite3.connect('member.db')
    c = conn.cursor()
    c.execute("SELECT * FROM STOCKS WHERE email='{}'".format(email))
    user = c.fetchall()
    conn.commit()
    conn.close()
    stocks = []
    for i in user:
        stock_name = i[1]
        stock_piece = i[2]
        stocks.append((stock_name,stock_piece))
    return stocks
