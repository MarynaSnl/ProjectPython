def creating_table(file_name, cursor, connection):
    if isfile(file_name):
        file = open(file_name)
        ss = file.read()
        cursor.execute(ss)
        connection.commit()
        file.close()
        ###### insert data in Frends
        return True
    else:    
        return False
    
    file_name = file_name.replace('.txt', '1.txt')
    if isfile(file_name):
        print(file_name)
        file = open(file_name, "r")
        ss = file.read()
        cursor.executescript(ss)
        connection.commit()
        file.close()
        return True
    else:    
        return False