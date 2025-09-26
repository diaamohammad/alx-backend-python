import sqlite3

class ExecuteQuery():

    def __init__(self,db_name,query,parmas=None):
        self.db_name= db_name
        self.conn = None
        self.query = query
        self.parmas = parmas if parmas else []
        self.curosr = None


    def enter(self,*args,**kwargs):

        self.conn = sqlite3.connect('db_users')
        self.curosr = self.conn.cursor()
        self.curosr.execute(self.query,self.parmas)
        results = self.curosr.fetchall()
        return results

    
    def __exit__(self,exc_type, exc_value, traceback):

        if self.conn:
            return self.conn.close()

query = "select * from users where age > ?"
parmas = (25,)

       
with ExecuteQuery('db_users',query,parmas) as result:
    for row in result:
       print(row)