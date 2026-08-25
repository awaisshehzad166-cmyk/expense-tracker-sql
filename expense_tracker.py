import sqlite3
connection=sqlite3.connect("expense.db")
connection.row_factory = sqlite3.Row
cursor=connection.cursor()
print("database connected successfully")
cursor.execute("""create table if not exists expenses(
id int primary key not null,
title varchar(50),
amount double,
catagory varchar(50),
expense_date date
);""")
connection.commit()
def add_expenses():
	id=int(input("enter the expense id:"))
	title=input("enter the expense title:")
	amount=float(input("enter the expense amount:"))
	catagory=input("enter the expense catagory:")
	date=input("enter the date in format(DD/MM/YY):")
	cursor.execute("""insert into expenses
	values
	(?,?,?,?,?)""",(id,title,amount,catagory,date))
	connection.commit()
def view_expenses():
	cursor.execute("""select * from expenses""")
	expenses=cursor.fetchall()
	for expense in expenses:
		print(dict(expense))
def search_expenses():
	id=int(input("enter the id of expense you want to search:"))
	cursor.execute("""select * from expenses
	where id=?""",(id,))
	expenses=cursor.fetchone()
	if expenses:
		print(dict(expenses))
	else:
		print("expense not found")
def update_expenses():
	id=int(input("enter the id of expense you want to update:"))
	new_title=input("enter the new title:")
	new_amount=float(input("enter the new amount:"))
	new_catagory=input("enter the new catagory:")
	new_date=input("enter the new date(DD/MM/YY):")
	cursor.execute("""update expenses
	set title=?,amount=?,catagory=?,expense_date=?
	where id=?""",(new_title,new_amount,new_catagory,new_date,id))
	connection.commit()
	print("expense updated successfully")
def delete_expenses():
	id=int(input("enter the id of expense you want to delete:"))
	cursor.execute("""delete from expenses
	where id=?""",(id,))
	connection.commit()
	print("expense deletes successfully")
def view_statics():
	cursor.execute("""select count(id) from expenses""")
	count=cursor.fetchone()[0]
	cursor.execute("""select sum(amount) from expenses""")
	sum=cursor.fetchone()[0]
	cursor.execute("""select avg(amount) from expenses""")
	avg=cursor.fetchone()[0]
	cursor.execute("""select amount from expenses order by amount desc limit 1""")
	highest=cursor.fetchone()[0]
	cursor.execute("""select amount from expenses order by amount asc limit 1""")
	lowest=cursor.fetchone()[0]
	cursor.execute("""select catagory,sum(amount) from expenses group by catagory""")
	catagory=cursor.fetchall()
	print("total number of expenses:",count)
	print("total expense amount:", sum)
	print("avg of expenses:",avg)
	print("highest amount of expenses:",highest)
	print("lowest amount of expenses:",lowest)
	for expense in catagory:
		print(dict(expense))
while True:
	print("enter 1 for add expenses")
	print("enter 2 for view expenses")
	print("enter 3 for search expenses")
	print("enter 4 for update expenses")
	print("enter 5 for delete expenses")
	print("enter 6 for view statics")
	print("enter 7 for exit")
	choice=int(input("enter your choice:"))
	if choice==1:
		add_expenses()
	elif choice==2:
		view_expenses()
	elif choice==3:
		search_expenses()
	elif choice==4:
		update_expenses()
	elif choice==5:
		delete_expenses()
	elif choice==6:
		view_statics()
	elif choice==7:
		print("good bye program terminated")
		break
	else:
		print("enter the right choice")
