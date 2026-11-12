# To connect idle to PostgreSQL

import psycopg2

conn = psycopg2.connect(
    database="python",
    user="postgres",
    password="1234",
    host="localhost",
    port="5432"
)

print("DB Connected Successfully")

# To create table in database
cur = conn.cursor()
#
# cur.execute("""
# CREATE TABLE employee(
#     id INT PRIMARY KEY,
#     name VARCHAR(50),
#     salary FLOAT
#     )
# """)
#
# conn.commit()
# print("Table Created Successfully")

#
# # To insert one value in the table
# cur.execute(
# "INSERT INTO employee VALUES(%s,%s,%s)",
# (108,'Gowsik',50000)
# )
# conn.commit()
#
#
# # To insert multiple value in the table
# data=[
#     (103,'Sabari',40000),
#     (104,'Karthi',50000),
#     (105,'Kowsalya',60000)]
#
# cur.executemany(
# "INSERT INTO employee VALUES(%s,%s,%s)",
# data
# )
# conn.commit()
# print("Values Added Successfully")


# # To Retrieve records
# cur.execute("SELECT * FROM employee")
#
# rows = cur.fetchall()
#
# for row in rows:
#     print(row)


# To update the table values
# cur.execute(
# "UPDATE employee "
# "   SET salary=%s "
# "   WHERE id=%s",
# (70000,101)
# )
#
# conn.commit()
# print("DB Updated Successfully")



# To delete a record in the table
# cur.execute(
#     "DELETE FROM employee "
#     "WHERE id=%s",
#     (108,)
# )
# conn.commit()
# print("successfully deleted")


# To drop the table:
cur.execute("DROP TABLE employee")
conn.commit()

#
# To close the connection:
cur.close()
conn.close()
print("DB Disconnected Successfully")


