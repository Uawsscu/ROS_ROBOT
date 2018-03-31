import sqlite3
def create_1():
    with sqlite3.connect("Robot_Test.db") as con:
        sql_cmd = """
            create table ActionName(Name TEXT PRIMARY KEY,ID int)
        """
        con.execute(sql_cmd)

def create_2():
    with sqlite3.connect("Robot_Test.db") as con:
        sql_cmd = """
            create table StepAction(ID,M1 int,M2 int,M3 int,M4 int,M5 int,M6 int,M7 int,M8 int,FOREIGN KEY(ID) REFERENCES FK_1(ID))
        """
        con.execute(sql_cmd)


if __name__ == '__main__':
    create_2()


    def callback_List(data, AA):
        A = data.data
        B = A.split(', ')
        D = []
        for i in B:
            C = int(i)
            D.append(C)

        with sqlite3.connect("Test_PJ1.db") as con:
            data = str(D)
            cut = data[2:]
            print cut
            s = "insert into StepAction(ID,Step,M1,M2) values (" + str(AA) + + "," + cut
            print s
            con.execute(s)


    def select_1(data):
        with sqlite3.connect("Test_PJ1.db") as con:
            cur = con.cursor()
            cur.execute("SELECT " + "ID" + " FROM ActionName where " + "Name" + "=?", (data.data,))
            # con.execute(sql_cmd)
            rows = cur.fetchone()
            for element in rows:
                return element



def callback_Talk(data):

	x = np.int_(data.data)
	with sqlite3.connect("Test_PJ1.db") as con:
		sql_cmd = """
			insert into ActionName(ID,Name) values (Null,?);
		"""
		con.execute(sql_cmd, x)

	print(data.data)
