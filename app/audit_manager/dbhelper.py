import sqlite3
import constants


def create_conn():
    try:
        con = sqlite3.connect(constants.SQLITE_DB)
        print(constants.SQLITE_DB)
        print(sqlite3.version)
        return con
    except Exception as e:
        print(f"Error occurred while connecting to db -> {e}")
        return None


if __name__ == '__main__':
    conn = create_conn()
    sql_create_projects_table = """ CREATE TABLE IF NOT EXISTS auditLog (
                                        cust_id text NOT NULL,
                                        customer_name text NOT NULL,
                                        cost_involved Decimal(10,2),
                                        audit_comment text,
                                        customer_comment text,
                                        customer_contact char(50)
                                    ); """
    conn.execute(sql_create_projects_table)
    conn.commit()
    conn.close()
