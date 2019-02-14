import getpass
import psycopg2
from prettytable import PrettyTable

db = psycopg2.connect(host="localhost",user="postgres",password="akash",database="log")
cursor = db.cursor()

#USER AUTHENTICATION 00 
def auth_user():
    print("\n\n")
    print("======================")
    print("      USER LOGIN      ")
    print("======================")
    un = str(input('Enter Username:'))
    ps = getpass.getpass('Enter Password:')
    if un == 'akash' and ps == 'akash':
        home()
        print("\n\n")
    else:
        print("Wrong username or password")
        auth_user()

#HOME 01
def home():
    print("\n\n")
    print("         HOME         ")
    print("======================")
    print(" 1)EDIT CUSTOMER      ")
    print("======================")
    print(" 2)PAID STATUS        ")
    print("======================")
    print(' 5)EXIT               ')
    print("======================")
    try:
        mns = int(input("Enter choice ==> "))
    except Exception:
        print("Re-enter the data with numeric value")
        home()

    if mns == 1:
        edits()
    elif mns == 2:
        paid_status()
    elif mns == 3:
        exit()
    else:
        print('invalid input')
        home()

#EDIT MENU 10
def edits():
    print("\n\n")
    print("EDITING CUSTOMER")
    print("===================")
    print('  1)INSERT ROW')  
    print('===================')
    print('  2)UPDATE ROW')
    print('===================')
    print('  3)REMOVE DATA')
    print('===================')
    print('  4)DISPLAY')
    print('===================')
    print('  5)HOME')
    print('===================')
    try:
        sws = int(input("  Enter Choice ==> "))
    except Exception:
        print("Re-enter the data with numeric value")
        edits()

    print("=====================")
    if sws == 1:
        menu1()
    elif sws == 2:
        menu2()
    elif sws == 3:
        menu3()
    elif sws == 4:
        menu4()
    elif sws == 5:
        home()
    else:
        print('invalid input')
        edits()

#MENU1 11
def menu1():
    print("\n\n")
    print("           INSERT DATA           ")
    print('=================================')
    try:
        ids = int(input("Enter ID:"))
    except Exception:
        print("Enter numeric values only")
        menu1()
    try:
        name = str(input("Enter Name:"))
        phone = int(input("Enter Phone number:"))
    except Exception:
        print("Enter numbers only")
        menu1()
    try:
        street = str(input("Enter Street:"))
        cid = str(input("Enter CID:"))
        stb = str(input("Enter STB:"))
    finally:
        print('====================================================')
        sql1 = ('INSERT INTO customers(id,name,phone,street,cid,stb) VALUES(%s,%s,%s,%s,%s,%s);')
        vals = ids,name,phone,street,cid,stb
        cursor.execute(sql1,vals)
        db.commit()
        t = PrettyTable(['ID','NAME','PHONE','STREET','CID','STB'])
        t.add_row(vals)
        print(t)
        print('=====================================================')
        print('record successfully uploaded')
        edits()

#UPDATES NAME  121
def update_name():
    ids = int(input('Enter id:'))
    name = str(input('Enter name:'))
    sql = 'UPDATE customers SET name=%s WHERE id=%s'; val = name,ids
    cursor.execute(sql,val)
    db.commit()
    print('successfully updated')
    print("==============================")

#UPDATES PHONE 122
def update_phone():
    ids = int(input('Enter id:'))
    phone = str(input('Enter Phone:'))
    sql = 'UPDATE customers SET phone=%s WHERE id=%s'; val = phone,ids
    cursor.execute(sql,val)
    db.commit()
    print('successfully updated')
    print("==============================")

#UPDATES STREET 125
def update_street():
    ids = int(input('Enter id:'))
    street = str(input('Enter street:'))
    sql = 'UPDATE customers SET street=%s WHERE id=%s'; val = street,ids
    cursor.execute(sql,val)
    db.commit()
    print('successfully updated')
    print("==============================")

#UPDATES CID 124
def update_cid():
    ids = int(input('Enter id:'))
    cid = str(input('Enter cid:'))
    sql = 'UPDATE customers SET cid=%s WHERE id=%s'; val = cid,ids
    cursor.execute(sql,val)
    db.commit()
    print('successfully updated')
    print("==============================")

#UPDATES STB 123
def update_stb():
    ids = int(input('Enter id:'))
    stb = str(input('Enter stb:'))
    sql = 'UPDATE customers SET stb=%s WHERE id=%s'; val = stb,ids
    cursor.execute(sql,val)
    db.commit()
    print('successfully updated')
    print("==============================")

#UPDATE ALL FIELDS 126
def update_all():
    ids = int(input('Enter id:'))
    name = str(input('Enter name:'))
    phone = str(input('Enter phone:'))
    stb = str(input('Enter stb:'))
    cid = str(input('Enter cid:'))
    street = str(input('Enter street:'))
    sql = 'UPDATE customers SET name=%s,phone=%s,street=%s,cid=%s,stb=%s WHERE id=%s'; val = name,phone,street,cid,stb,ids
    cursor.execute(sql,val)
    db.commit()
    print('successfully updated') 
    print("==============================")

#MENU2 120
def menu2():
    print("\n\n")
    print("         UPDATE DATA          ")
    print("==============================")
    print("  1)NAME\n  2)PHONE\n  5)STREET\n  4)CID\n  3)STB\n  6)ALL")
    print("==============================")
    try:
        ins = int(input('Enter choice to modify ==> '))
    except Exception:
        print("Re-enter the data with numeric value")
        menu2()

    print("==============================")
    if ins == 1:
        update_name()
        edits()
    elif ins == 2:
        update_phone()
        edits()
    elif ins == 3:
        update_street()
        edits()
    elif ins == 4:
        update_cid()
        edits()
    elif ins == 5:
        update_stb()
        edits()
    elif ins == 6:
        update_all()
        edits()
    else:
        print("Invalid input")
        edits()

#REMOVE ROW 131
def remove_row():
    ids = int(input('Enter id:'))
    sql = 'DELETE FROM customers WHERE id=%s' % ids
    cursor.execute(sql)
    db.commit()
    print('successfully removed')
    print('==============================') 

#REMOVE ALL DATA 132
def remove_all():
    sql = 'TRUNCATE TABLE customers'
    cursor.execute(sql)
    db.commit()
    print('successfully removed')
    print('==============================')    

#MENU3 130
def menu3():
    print("\n\n")
    print("    REMOVE DATA    ")
    print('===================')
    print("     1)By ID")
    print('===================')
    print("     2)ALL DATA")
    print('===================')
    try:
        ins = int(input('Enter choice to display ==> '))
    except Exception:
        print("Re-enter the data with numeric value")
        menu3()

    if ins == 1:
        remove_row()
        edits()
    elif ins == 2:
        remove_all()
        edits()
    else:
        print('invalid input')
        edits()

#DISPLAY ONLY BY ID 141
def Id():
    ids = int(input("Enter id:"))
    sql = 'SELECT id,name,phone,stb,cid,street,cid,stb FROM customers WHERE id=%s' % ids 
    cursor.execute(sql)
    r = cursor.fetchone()
    t = PrettyTable(['ID','NAME','PHONE','STREET','CID','STB'])
    t.add_row(r)
    print(t)

#DISPLAY ALL DATA 142 
def aLL():
    cursor.execute('SELECT id,name,phone,street,cid,stb FROM customers ORDER BY id')
    r = cursor.fetchall()
    t = PrettyTable(['ID','NAME','PHONE','STREET','CID','STB'])
    for i in r:
        t.add_row(i)
    print(t)

#MENU4 140 
def menu4():
    print("\n\n")
    print(" DISPLAY DATA")
    print('===============')
    print(" 1)ID")
    print('===============')
    print(" 2)ALL DATA")
    print('===============')
    try:
        ins = int(input('Enter choice to display ==> '))
    except Exception:
        print("Re-enter the data with numeric value")
        menu4()
        
    if ins == 1:
        print('=================================================================')
        Id()
        print('=================================================================')
        edits()
    elif ins == 2:
        print('=================================================================')
        aLL()
        print('=================================================================')
        edits()
    else:
        print('Invalid input')
        menu4()

from prettytable import PrettyTable
import psycopg2
from Main import home
db = psycopg2.connect(host="localhost",user="postgres",password="akash",database="log")
cursor = db.cursor()

def paid_status():

    print("\n\n")
    print("      PAID STATUS      ")
    print("=======================")
    print("    1)POST  STATUS     ")
    print("=======================")
    print("    2)CHECK STATUS     ")
    print("=======================")
    print("    3)HOME             ")
    print("=======================")
    try:
        pas = int(input("Enter choice ==> "))
    except Exception:
        print("Re-enter the data with numeric value")
        paid_status()
    
    if pas == 1:
        post_status()
        paid_status()
    elif pas == 2:
        check_status_all()
        paid_status()
    elif pas ==3:
        home()
    else:
        print('invalid input')

def jan_amt():
    try:
        ids = int(input("Enter id:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    try:
        amt = int(input('Enter amount:'))
        com = str(input("Enter comments:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    sql = 'INSERT INTO jan_table(id,january,comments) VALUES(%s,%s,%s)' 
    val =  ids, amt, com
    cursor.execute(sql,val)
    print('Status posted successfully')

def feb_amt():
    try:
        ids = int(input("Enter id:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    try:
        amt = int(input('Enter amount:'))
        com = str(input("Enter comments:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    sql = 'INSERT INTO feb_table(id,feburary,comments) VALUES(%s,%s,%s)' 
    val =  ids, amt, com
    cursor.execute(sql,val)
    print('Status posted successfully')

def mar_amt():
    try:
        ids = int(input("Enter id:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    try:
        amt = int(input('Enter amount:'))
        com = str(input("Enter comments:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    sql = 'INSERT INTO mar_table(id,march,comments) VALUES(%s,%s,%s)' 
    val =  ids, amt, com
    cursor.execute(sql,val)
    print('Status posted successfully')

def apr_amt():
    try:
        ids = int(input("Enter id:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    try:
        amt = int(input('Enter amount:'))
        com = str(input("Enter comments:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    sql = 'INSERT INTO apr_table(id,april,comments) VALUES(%s,%s,%s)' 
    val =  ids, amt, com
    cursor.execute(sql,val)
    print('Status posted successfully')

def may_amt():
    try:
        ids = int(input("Enter id:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    try:
        amt = int(input('Enter amount:'))
        com = str(input("Enter comments:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    sql = 'INSERT INTO may_table(id,may,comments) VALUES(%s,%s,%s)' 
    val =  ids, amt, com
    cursor.execute(sql,val)
    print('Status posted successfully')

def jun_amt():
    try:
        ids = int(input("Enter id:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    try:
        amt = int(input('Enter amount:'))
        com = str(input("Enter comments:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    sql = 'INSERT INTO jun_table(id,june,comments) VALUES(%s,%s,%s)' 
    val =  ids, amt, com
    cursor.execute(sql,val)
    print('Status posted successfully')

def jul_amt():
    try:
        ids = int(input("Enter id:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    try:
        amt = int(input('Enter amount:'))
        com = str(input("Enter comments:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    sql = 'INSERT INTO july_table(id,july,comments) VALUES(%s,%s,%s)' 
    val =  ids, amt, com
    cursor.execute(sql,val)
    print('Status posted successfully')

def aug_amt():
    try:
        ids = int(input("Enter id:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    try:
        amt = int(input('Enter amount:'))
        com = str(input("Enter comments:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    sql = 'INSERT INTO aug_table(id,august,comments) VALUES(%s,%s,%s)' 
    val =  ids, amt, com
    cursor.execute(sql,val)
    print('Status posted successfully')

def sep_amt():
    try:
        ids = int(input("Enter id:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    try:
        amt = int(input('Enter amount:'))
        com = str(input("Enter comments:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    sql = 'INSERT INTO sep_table(id,september,comments) VALUES(%s,%s,%s)' 
    val =  ids, amt, com
    cursor.execute(sql,val)
    print('Status posted successfully')

def oct_amt():
    try:
        ids = int(input("Enter id:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    try:
        amt = int(input('Enter amount:'))
        com = str(input("Enter comments:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    sql = 'INSERT INTO oct_table(id,october,comments) VALUES(%s,%s,%s)' 
    val =  ids, amt, com
    cursor.execute(sql,val)
    print('Status posted successfully')

def nov_amt():
    try:
        ids = int(input("Enter id:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    try:
        amt = int(input('Enter amount:'))
        com = str(input("Enter comments:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    sql = 'INSERT INTO nov_table(id,november,comments) VALUES(%s,%s,%s)' 
    val =  ids, amt, com
    cursor.execute(sql,val)
    print('Status posted successfully')

def dec_amt():
    try:
        ids = int(input("Enter id:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()   
    try:
        amt = int(input('Enter amount:'))
        com = str(input("Enter comments:"))
    except Exception:
        print("Re-enter the data with numeric value")
        post_status()
    sql = 'INSERT INTO dec_table(id,december,comments) VALUES(%s,%s,%s)' 
    val =  ids, amt, com
    cursor.execute(sql,val)
    print('Status posted successfully')

def check_status_all():
    pass

def post_status():
    print("\n\n")
    print("      POST STATUS      ")
    print("=======================")
    print("      1)JANAUARY       ")
    print("=======================")
    print("      2)FEBURARY       ")
    print("=======================")
    print("      3)MARCH          ")
    print("=======================") 
    print("      4)APRIL          ")
    print("=======================") 
    print("      5)MAY            ")
    print("=======================") 
    print("      6)JUNE           ")
    print("=======================") 
    print("      7)JULY           ")
    print("=======================") 
    print("      8)AUGUST         ")
    print("=======================") 
    print("      9)SEPTEMBER      ")
    print("=======================") 
    print("     10)OCTOBER        ")
    print("=======================") 
    print("     11)NOVEMBER       ")
    print("=======================") 
    print("     12)DECEMBER       ")
    print("=======================")
    print("     13)HOME           ")
    print("=======================")  

    ins = int(input("Enter choice ==> "))
    print("=======================") 

    if ins == 1:
        jan_amt()
        post_status()

    elif ins == 2:
        feb_amt()
        post_status()
    elif ins == 3:
        mar_amt()
        post_status()

    elif ins == 4:
        apr_amt()
        post_status()

    elif ins == 5:
        may_amt()
        post_status()

    elif ins == 6:
        jun_amt()
        post_status()

    elif ins == 7:
        jul_amt()
        post_status()

    elif ins == 8:
        aug_amt()
        post_status()

    elif ins == 9:
        sep_amt()
        post_status()

    elif ins == 10:
        oct_amt()
        post_status()

    elif ins == 11:
        nov_amt()
        post_status()

    elif ins == 12:
        dec_amt()
        post_status()

    elif ins == 13:
        home()
    else:
        print("Invalid input")
        post_status()

#MAIN METHOD
if __name__=="__main__":
    auth_user()



