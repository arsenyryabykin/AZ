import sqlitedb
import time
import os.path
#import openpyxl
from make_docx import make_shelves_doc, make_case_operations_doc, make_az_operations_doc
from common import case_content, shelf_1, shelf_2, shelf_3, case_1, case_2,\
case_3, case_4, case_5, case_6, case_7, az

print("1: Полная загрузка имитационной зоны")
T = int(input())
if(T == 1):
    ### Проверка наличия входных файлов ############################
    all_files_exist = os.path.isfile('shelf_1.txt')\
                      and os.path.isfile('shelf_2.txt')\
                      and os.path.isfile('shelf_3.txt')\
                      and os.path.isfile('load_schedule.txt')

    if(not all_files_exist):
        print("Ошибка: отсутствуют входные файлы.")
        exit()
    else:
        # Чтение данных по стеллажам из входных файлов
        sqlitedb.read_shelves_data('shelf_1.txt', 1, shelf_1)
        sqlitedb.read_shelves_data('shelf_2.txt', 2, shelf_2)
        sqlitedb.read_shelves_data('shelf_3.txt', 3, shelf_3)
        print("Чтение входных данных")
#
#     #################################################################
#     # Подключение к БД
    sqlitedb.sql_start()

    # Создание таблиц
    sqlitedb.make_shelves()
    sqlitedb.make_cases()
    sqlitedb.make_cases_loading()
    sqlitedb.make_az_loading()




#
#     #################################################################
    # Вставка входных данных в БД
    sqlitedb.insert_shelves_data(shelf_1)
    sqlitedb.insert_shelves_data(shelf_2)
    sqlitedb.insert_shelves_data(shelf_3)

    # Создание документа по исходной конфигурации стелажей
    make_shelves_doc()

    #################################################################
    # Сопоставление типов ТВС ячейкам чехла
    sqlitedb.make_cases_data(1, case_1, case_content[0])
    sqlitedb.make_cases_data(2, case_2, case_content[1])
    sqlitedb.make_cases_data(3, case_3, case_content[2])
    sqlitedb.make_cases_data(4, case_4, case_content[3])
    sqlitedb.make_cases_data(5, case_5, case_content[4])
    sqlitedb.make_cases_data(6, case_6, case_content[5])
    sqlitedb.make_cases_data(7, case_7, case_content[6])

    # Вставка типов в БД
    sqlitedb.insert_cases_data(case_1)
    sqlitedb.insert_cases_data(case_2)
    sqlitedb.insert_cases_data(case_3)
    sqlitedb.insert_cases_data(case_4)
    sqlitedb.insert_cases_data(case_5)
    sqlitedb.insert_cases_data(case_6)
    sqlitedb.insert_cases_data(case_7)

#     #################################################################
    # Заполнение чехлов согласно графику загрузки из стеллажей
    sqlitedb.fill_case(1)
    sqlitedb.fill_case(2)
    sqlitedb.fill_case(3)
    sqlitedb.fill_case(4)
    sqlitedb.fill_case(5)
    sqlitedb.fill_case(6)
    sqlitedb.fill_case(7)


    sqlitedb.make_az_data(az)
    sqlitedb.insert_az_data(az)
    sqlitedb.fill_az()
#
#     #################################################################
    # Создание документа по перегрузочным операциям Стеллаж -> Чехол
    make_case_operations_doc()
    # Создание документа по перегрузочным операциям Чехол -> АЗ
    make_az_operations_doc()

    #################################################################
else:
    print("Выход")
    time.sleep(3)
    exit()



