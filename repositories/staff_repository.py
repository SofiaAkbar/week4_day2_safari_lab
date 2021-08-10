from db.run_sql import run_sql
from models.staff import Staff

def delete_all():
    sql = "DELETE FROM staff"
    run_sql(sql)


def delete(id):
    sql = "DELETE FROM staff WHERE id = %s"
    values = [id]
    run_sql(sql, values)


def save(staff):
    sql = "INSERT INTO staff (name, start_date, dept, performance) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [staff.name, staff.start_date, staff.dept, staff.performance]
    results = run_sql(sql, values)
    id = results[0]['id']
    staff.id = id
    return staff


def select_all():
    staff = [] 

    sql = "SELECT * FROM staff"
    results = run_sql(sql)

    for row in results:
        person = Staff(row['name'], row['start_date'], row['dept'], row['performance'], row['id'])
        staff.append(person)
    return staff


def select(id):
    person = None 
    sql = "SELECT * FROM staff WHERE id = %s"
    values = [id]
    result = run_sql(sql, values)[0]

    if result is not None:
        person = Staff(result['name'], result['start_date'], result['dept'], result['performance'], result['id'])

    return person


def update(staff):
    sql = "UPDATE staff SET (name, start_date, dept, performance) = (%s, %s, %s, %s) WHERE id = %s"
    values = [staff.name, staff.start_date, staff.dept, staff.performance]
    run_sql(sql, values)