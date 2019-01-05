fruits = init_table()
valuelist = [{'name':plum','color':'purple'},record2]
stmt = insert(fruits).values()
results = con.execute(stmt,valuelist)
print(results.rowcount)


#############################
stmt = select([artist])
stmt = stmt.where(or_(artist.columns.ArtistId < 5, artist.columns.ArtistId > 273))

for res in con.execute(stmt):

	print(res.Name)

#############################

s = select([cookies])
s = s.order_by(cookies.columns.rating)
for r in con.execute(s):
	print(r.rating, r.cost, r.cookie_type)

#############################

metadata = init_table()
metadata.creat_all(engine)
print(engine.table_names())


#############################

fruits = init_table()
valuelist = [{'name':'plum', 'color':'purple'},record2]
stmt = insert(fruits).values()
results = con.execute(stmt,valuelist)
print(results.rowcount)

#############################

metadata = check_exists(fruits)
fruits = Table('fruits',metadata, Columns('name', String(30)),Column('color',String(30),default = 'red'))
metadata.creat_all(engine)
print(engine.table_names())

#############################

from sqlalchemy import select
stmt = select([album])
print(con.execute(stmt)).fetchmany(size=2))

#############################

stmt = select([func.count(track.columns.Name.distinct())])
results = con.execute(stmt).fetchall()
print(results)

#############################

stmt = select([album.columns.Title])
results = con.execute(stmt).fetchall()
print(results[:3])

#############################

sessions['devices'] = sessions['DEVICES'].apply(str.capitalize)
print(sessions)