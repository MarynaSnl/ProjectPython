def creating_table(file_name, cursor, connection):
    file = open(file_name)
    ss = file.read()
    cursor.execute(ss)
    connection.commit()
    file.close()
    
    file_name = file_name.replace('.txt', '1.txt')
    file = open(file_name, "r")
    ss = file.read()
    cursor.executescript(ss)
    connection.commit()
    file.close()
