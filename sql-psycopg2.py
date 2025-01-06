import psycopg2

# Connect to an existing database - (** create database)
connection = psycopg2.connect(database="")

# Open a cursor to perform database operations
cursor = connection.cursor()

# fetch the results (multiple)

# fetch the results (single)
# result = cursor.fetchone()

# Close connection with the database
connection.close()

# Print the result
for result in results:
    print(result)
    
    
    
    
# link to this - https://learn.codeinstitute.net/courses/course-v1:code_institute+WWDBMS+3/courseware/c0c31790fcf540539fd2bd3678b12406/22de863d16b346c6bdbb1945f63770ea/?child=first
    