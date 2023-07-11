import sqlvalidator

sql = "SELECT name, age FROM users WHERE age > 18"

# Format the query
formatted_sql = sqlvalidator.format_sql(sql)
print(formatted_sql)

# Parse the query
sql_query = sqlvalidator.parse(sql)

# Check if the query is valid
if sql_query.is_valid():
    print("The query is valid.")
else:
    print("The query is invalid.")
    print(sql_query.errors)
