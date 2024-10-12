import sqlite3
from common import shelf_coords, case_content

def sql_start():
    global conn, cur
    conn = sqlite3.connect('imitators.db')
    if conn:
        print("Успешное подключение к БД")
    cur = conn.cursor()

def make_shelves():
    cur.execute('''DROP TABLE IF EXISTS shells''')
    cur.execute('''CREATE TABLE IF NOT EXISTS shells(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                shelf_number INTEGER,
                coordinate TEXT,
                tvs_number TEXT,
                tvs_type TEXT,
                suz_number TEXT,
                suz_type TEXT)''')
    conn.commit()

def make_cases():
    cur.execute('''DROP TABLE IF EXISTS cases''')
    cur.execute('''CREATE TABLE IF NOT EXISTS cases(
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                case_number INTEGER,
                case_coordinate TEXT,
                az_coordinate TEXT UNIQUE,
                tvs_number TEXT,
                tvs_type TEXT,
                suz_number TEXT,
                suz_type TEXT)''')
    conn.commit()

def make_cases_loading():
    cur.execute('''DROP TABLE IF EXISTS case_operations''')
    cur.execute('''CREATE TABLE IF NOT EXISTS case_operations(
                   operation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                   shelf_number_from INTEGER,
                   shelf_coordinate_from TEXT,
                   case_number_to INTEGER,
                   case_coordinate_to TEXT,
                   tvs_number TEXT,
                   tvs_type TEXT,
                   suz_number TEXT,
                   suz_type TEXT)''')
    conn.commit()

###########################################################################################3
# Создание таблицы БД с загрузкой АЗ из чехлов
def make_az_loading():
    cur.execute('''DROP TABLE IF EXISTS az_operations''')
    cur.execute('''CREATE TABLE IF NOT EXISTS az_operations(
                    operation_id INTEGER PRIMARY KEY AUTOINCREMENT,
                    case_number_from INTEGER,
                    case_coordinate_from TEXT,
                    az_coordinate_to TEXT,
                    tvs_number TEXT,
                    tvs_type TEXT,
                    suz_number TEXT,
                    suz_type TEXT)''')
    conn.commit()

# Создание кортежа основных данных для занесения в таблицу Чехлы -> АЗ
def make_az_data(az):
    for case_number, case_cont in enumerate(case_content, start = 1):
        for coord, content in enumerate(case_cont, start = 1):
            data = (case_number, coord, content[0])
            az.append(data)

# Вставка основных строк в таблицу Чехлы -> АЗ
def insert_az_data(az):
    cur.executemany('''INSERT INTO az_operations(case_number_from, case_coordinate_from, az_coordinate_to)
    VALUES(?, ?, ?);''', az)
    conn.commit()

def fill_az():
    #######################################################################

    for i in range(1, 164):
        cur.execute('''SELECT case_number_from, case_coordinate_from
                       FROM az_operations
                       WHERE operation_id = ?;''', (i,))
        coords = cur.fetchone()

        cur.execute('''SELECT tvs_number, tvs_type, suz_number, suz_type
                       FROM cases
                       WHERE case_number = ? AND case_coordinate = ?;''', (coords[0], coords[1]))
        tvs_data = cur.fetchone()
        # print(tvs_data)
        if(tvs_data[2] != None):
            cur.execute('''UPDATE az_operations
                           SET tvs_number = ?,
                               tvs_type = ?,
                               suz_number = ?,
                               suz_type = ?
                           WHERE case_number_from = ? AND
                                 case_coordinate_from = ?;''', (tvs_data[0], tvs_data[1],
                                                               tvs_data[2], tvs_data[3],
                                                               coords[0], coords[1]))
        elif(tvs_data[2] == None):
            cur.execute('''UPDATE az_operations
                           SET tvs_number = ?,
                               tvs_type = ?
                           WHERE case_number_from = ? AND
                                 case_coordinate_from = ?''', (tvs_data[0], tvs_data[1],
                                                               coords[0], coords[1]))

        conn.commit()


###########################################################################################3

# Чтение данных по стеллажам из файлов
def read_shelves_data(file, shell_number, shell):
    with open(file, 'r', encoding='utf-8') as f:
        for coordinate in shelf_coords:
            line = f.readline()
            if not line:
                break
            result = line.split()
            tvs = result[0]
            tvs_type = tvs[-2:]
            if tvs == 'empty':
                tvs_type = None
            if(len(result) == 1):
                suz = None
                suz_type = None
                #tvs_type = None
            else:
                suz = result[1]
                suz_type = suz[-2:]

            data = (shell_number, coordinate, tvs, tvs_type, suz, suz_type)
            shell.append(data)

# Вставка прочитанных данных по стеллажам в БД
def insert_shelves_data(shell):
    cur.executemany('''INSERT INTO shells(shelf_number, coordinate, tvs_number,
    tvs_type, suz_number, suz_type ) VALUES(?, ?, ?, ?, ?, ?);''', shell)
    conn.commit()

# Сопоставление типов ТВС ячейкам чехла
def make_cases_data(case_number, case, case_cont):
    for i, el in enumerate(case_cont, 1):
        if(len(el) == 3):
            data = (case_number, i, el[0], None, el[1], None, el[2])
        else:
            data = (case_number, i, el[0], None, el[1], None, None)
        case.append(data)

# Вставка данных по типам в чехлы
def insert_cases_data(case):
    cur.executemany('''INSERT INTO cases(case_number, case_coordinate, az_coordinate,
    tvs_number, tvs_type, suz_number, suz_type ) VALUES(?, ?, ?, ?, ?, ?, ?);''', case)
    conn.commit()

def fill_case(case_number):
    #######################################################################
    finish = 28 if case_number <= 6 else 2
    # Заполнение чехла case_number
    for i in range(1, finish):

        # Выбор типа ТВС и СУЗ для очередной ячейки чехла
        cur.execute('''SELECT tvs_type, suz_type
                    FROM cases
                    WHERE case_number = ? AND case_coordinate = ?;''', (case_number, i))
        tvs_type, suz_type = cur.fetchone()
        # print(tvs_type, suz_type)

        #######################################################################
        # Поиск в стеллажах необходимой ТВС и ПС СУЗ
        if (suz_type == None):
            cur.execute('''SELECT *
                            FROM shells
                            WHERE tvs_type = ? AND suz_type IS NULL
                            LIMIT 1;''', (tvs_type,))
            tvs_and_suz = cur.fetchone()

        elif(suz_type != None):
            cur.execute('''SELECT *
                            FROM shells
                            WHERE tvs_type = ? AND suz_type = ?
                            LIMIT 1;''', (tvs_type, suz_type))
            tvs_and_suz = cur.fetchone()

        # print(tvs_and_suz)

        cur.execute('''UPDATE cases
                        SET tvs_number = ?,
                            tvs_type = ?,
                            suz_number = ?,
                            suz_type = ?
                        WHERE case_number = ? AND case_coordinate = ?;''',
                    (tvs_and_suz[3], tvs_and_suz[4], tvs_and_suz[5], tvs_and_suz[6],
                     case_number, i))

        cur.execute('''UPDATE shells
                        SET tvs_number = 'empty',
                            tvs_type = NULL,
                            suz_number = NULL,
                            suz_type = NULL
                        WHERE shelf_number = ? AND coordinate = ?''', (tvs_and_suz[1], tvs_and_suz[2]))
        #####################################################################
        # Добавление произведенной операции в таблицу перекладываний Стеллаж -> Чехол

        cur.execute(''' INSERT INTO case_operations(shelf_number_from, shelf_coordinate_from,
                   case_number_to, case_coordinate_to, tvs_number, tvs_type,
                   suz_number, suz_type) VALUES(?, ?, ?, ?, ?, ?, ?, ?)''',
                    (tvs_and_suz[1], tvs_and_suz[2], case_number, i,
                     tvs_and_suz[3], tvs_and_suz[4], tvs_and_suz[5], tvs_and_suz[6]))

        conn.commit()
                       
                     
 




