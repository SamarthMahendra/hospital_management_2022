import pymongo
class patients:
    def __init__(self):
        pass
    def reg(self):
        print("Enter your name:")
        name=str(input())
        print("Enter your age:")
        age=int(input())
        self.insert(name,age)
    def dbconnect(self):
        mongohost = "localhost"
        mongoport = 27017
        connection = pymongo.MongoClient(mongohost, mongoport)
        print("----------DB connection Successful----------")
        return connection
    def dbclose(self,conection):
        conection.close()
        print("----------db connection closed successfully------")
        return


    def insert(self,name,age):
        connection=self.dbconnect()
        collection = connection["giraffe"]["students"]

        data=collection.insert_one({"name":name,"age":age})
        if data:
            print("**********Data inserted successfullly*********")
        self.dbclose(connection)    \

        return

    def displayall(self):
        print("----------Displaying all data in db----------- ")
        connection = self.dbconnect()
        collection = connection["giraffe"]["students"]
        d=collection.find({},{"_id":0})
        for i in d:
            print(i)
        self.dbclose(connection)
    def delete(self):

        connection = self.dbconnect()
        collection = connection["giraffe"]["students"]
        q={"age":77}
        collection.delete_one(q)
        self.displayall()
        self.dbclose(connection)


temp=patients()
temp.reg()
temp.displayall()
temp.delete()
