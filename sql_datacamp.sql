-- good_cookies = func.sum(cost([(cookies.columns.rate1 >= 7, cookies.columns.rate2)],else = 0))

-- Find the total cost of good cookies by summing the cost column for cookies with a rating of 7 or higher.
good_cookies = func.sum(case([(cookies.columns.rate1 >= 7, cookies.columns.cost)],else = 0))
s = select([good_cookies])
print(con.execute(s).fetchall())