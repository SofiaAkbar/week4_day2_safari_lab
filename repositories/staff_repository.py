from db.run_sql import run_sql
from models.staff import Staff

def delete_all():
    sql = "DELETE FROM staff_details"
    run_sql(sql)

def delete(id):
    sql = "DELETE FROM staff_details WHERE id = %s"
    values = [id]
    run_sql(sql, values)

def save(staff):
    sql = "INSERT INTO staff_details (name, start_date, dept, performance) VALUES (%s, %s, %s, %s) RETURNING *"
    values = [staff.name, staff.start_name, staff.dept, staff.performance]
    results = run_sql(sql, values)
    id = results[0]['id']
    staff.id = id
    return staff