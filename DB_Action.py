import sqlite3

def create_ActionName():
    with sqlite3.connect("DB_Project.db") as con:
        sql_cmd = """
            create table ActionName(ID INTEGER,Name TEXT PRIMARY KEY)
        """
        con.execute(sql_cmd)


def create_Buffer():
    with sqlite3.connect("DB_Project.db") as con:
        sql_cmd = """
            create table Buffer_Action(Motor1 int,Motor2 int,Motor3 int,Motor4 int,Motor5 int,Motor6 int,Motor7 int,Motor8 int,ID_Buff INTEGER PRIMARY KEY)

        """
        con.execute(sql_cmd)

def create_ActionRobot():
    with sqlite3.connect("DB_Project.db") as con:
        sql_cmd = """
            create table Action_Robot(ID int,stepAction int,Motor1 int,Motor2 int,Motor3 int,Motor4 int,Motor5 int,Motor6 int,Motor7 int,Motor8 int)
        """
        con.execute(sql_cmd)


if __name__ == '__main__':
    create_ActionRobot()
