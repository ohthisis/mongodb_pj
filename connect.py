import pymongo
import random

if __name__=="__main__":
    connection = pymongo.MongoClient("localhost", 27017)
    database = connection["test"]
    store = database["students"]

    try:
        id_number=random.randint(10,1000)
        user_email=str(input("Enter your email"))
        user_password=str(input("Enter your password"))
        data_form={"_id":id_number,"email":user_email,"password":user_password}
        total=store.insert_one(data_form)
        print("inserted data",total.inserted_id)
    except Exception as err:
        print("error")




