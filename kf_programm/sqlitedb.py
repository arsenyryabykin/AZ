import sqlite3

def get_az_data() -> dict:
    conn = sqlite3.connect('../imitators.db')
    cur = conn.cursor()

    cur.execute('''SELECT az_coordinate_to, tvs_number, suz_number
                FROM az_operations''')
    data = cur.fetchall()

    text_az_data = {}
    for coord, tvs, suz in data:
        text_az_data[coord] = (tvs, suz)

    return text_az_data
    # return data

if __name__ == "__main__":
    print(get_az_data())