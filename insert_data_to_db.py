import pymongo
import random

if __name__=="__main__":
    connection = pymongo.MongoClient("localhost", 27017)
    database = connection["test"]
    store = database["students"]

    for i in range(10):
        id_number = random.randint(10, 1000)
        user_email: str = "win"+str(i)+"@gmail.com"
        user_password: str = "123458"
        user_phone: int= 985890
        point:int=100
        info:str="User data is win"+str(i)+"id:"+str(id_number)

        data_form = {"_id": id_number, "email": user_email, "password": user_password,"phone":user_phone,"info":info,"point":point}
        total = store.insert_one(data_form)
        print("inserted data", total.inserted_id)





