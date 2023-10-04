import pymongo

collection=pymongo.MongoClient("localhost",27017)
database=collection["test"]
connection=database["students"]

if __name__=="__main__":
    r_email=input("Enter your email")
    for i in connection.find({},{"_id":0,"name":1}):#query
        print(i)
    for a in connection.find({},{"_id":0,"email":1}):
        if r_email==a["email"]:
            print("Invalid")
            break