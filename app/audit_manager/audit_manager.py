from dbhelper import create_conn
from publish import send_message
import uuid



class AuditLog:

    def __init__(self, customer_name, audit_comment, cost_involved):
        self.cust_id = uuid.uuid4()
        self.customer_name = customer_name
        self.audit_comment = audit_comment
        self.cost_involved = cost_involved
        self.customer_comment = None
        self.customer_contact = None

    # insert in log file
    def insert_log(self):
        dbconn = create_conn()
        if dbconn is None:
            print('Error acquiring connection !!! ')
            return None
        else:
            print(dbconn.execute("select * from auditLog"))
            insert_log = f'insert into auditLog  values ("{self.cust_id}", "{self.customer_name}","{self.audit_comment}",{self.cost_involved}, "{self.customer_comment}", "{self.customer_contact}")'
            print(insert_log)
            dbconn.execute(insert_log)
            dbconn.commit()
            dbconn.close()
        return self.cust_id

    def publish_message(self):
        """ put the message in the queue """
        message = ' '.join([self.customer_name, self.audit_comment, str(self.cost_involved), str(self.customer_comment),
                           str(self.customer_contact)])
        send_message(message=message)


if __name__ == '__main__':
    log = AuditLog('Vikash','test',500)
    log.customer_comment = " Audit Completed"
    log.customer_contact = 'abc@example.com'
    log.insert_log()
    log.publish_message()
