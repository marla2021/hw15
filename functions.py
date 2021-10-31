import sqlite3


def animal_by_id(itemid):
    con = sqlite3.connect("animal.db")
    cur = con.cursor()
    query1 = '''CREATE TABLE colors (
                ID INTEGER PRIMARY KEY AUTOINCREMENT,
                Name varchar(30) NOT NULL DEFAULT 'Noname')'''
    query2 = '''INSERT INTO colors (name) SELECT color1 FROM animals'''
    query3 = '''CREATE TABLE animal_colors (animal_id INT, color_id INT)'''
    query4 = '''INSERT INTO animal_colors
                SELECT animals."index", colors.id
                FROM animals JOIN colors on color1 = colors.name'''
    query5 = '''CREATE TABLE outcomes (outcome_id INTEGER PRIMARY KEY AUTOINCREMENT,
                outcome_subtype VARCHAR(50), outcome_month INT, outcome_year INT)'''
    query6 = '''INSERT INTO outcomes(outcome_subtype,outcome_month,outcome_year)
                SELECT outcome_subtype,outcome_month,outcome_year
                FROM animals GROUP BY outcome_subtype,outcome_month,outcome_year'''
    query7 = '''CREATE TABLE animal_types (ID INTEGER PRIMARY KEY AUTOINCREMENT,  Name VARCHAR(30))'''
    query8 = '''CREATE TABLE breed (ID INTEGER PRIMARY KEY AUTOINCREMENT,  Name VARCHAR(30))'''
    query9 = '''INSERT INTO animal_types (name) SELECT DISTINCT animal_type FROM animals'''
    query10 = '''INSERT INTO breed (name) SELECT DISTINCT breed FROM animals'''
    query11 = '''CREATE TABLE animals_new (ID INTEGER PRIMARY KEY AUTOINCREMENT, age_upon_outcome VARCHAR(30),
                 animal_id VARCHAR(30), type_id INT, name VARCHAR(30), breed_id INT, date_of_birth DATE,
                 outcome_id INT)'''
    query12 = '''INSERT INTO animals_new
                 SELECT "index", age_upon_outcome, animal_id, animal_types.id, animals.name, breed.id, date_of_birth, outcomes.outcome_id
                 FROM animals
                 LEFT JOIN animal_types ON animal_type = animal_types.name
                 LEFT JOIN breed ON animals.breed = breed.name
                 LEFT JOIN outcomes on animals.outcome_subtype = outcomes.outcome_subtype
                 AND animals.outcome_month = outcomes.outcome_month
                 AND animals.outcome_year = outcomes.outcome_year'''
    query13 = f'''SELECT age_upon_outcome, animal_id, animal_types.name, breed.name, date_of_birth 
                 FROM animals_new 
                 LEFT JOIN breed on animals_new.breed_id = breed.id
                 LEFT JOIN animal_types on animals_new.type_id = animal_types.id
                 WHERE animals_new.id = {itemid}'''

    cur.execute(query1)
    cur.execute(query2)
    cur.execute(query3)
    cur.execute(query4)
    cur.execute(query5)
    cur.execute(query6)
    cur.execute(query7)
    cur.execute(query8)
    cur.execute(query9)
    cur.execute(query10)
    cur.execute(query11)
    cur.execute(query12)
    cur.execute(query13)
    result = cur.fetchall()
    con.close()
    result_dict = {
        "age_upon": result[0][1],
        "animal_id": result[0][2],
        "name": result[0][3],
        "breed": result[0][4],
    }
    return result_dict