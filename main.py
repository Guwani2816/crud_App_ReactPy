from pymongo import MongoClient
# Replace <uri> with your MongoDB Atlas connection string 
uri = "mongodb+srv://Guwani:guwi@cluster1.dvkosoa.mongodb.net/"
client = MongoClient(uri)

#Replace <database-name> with the name of your database 
db = client["NIBM"]

#Replace <collection-name> with the name of your collection 
collection = db["NIC"]

#check the connection 
try:
    client.admin.command("ping")
    print("Pinged your deployment.You have successfully connected to MongoDB!")
except Exception as e:
    print(e)

document = {"name": "Daniel","age":36}

#Insert the document into the collection
insert_result = collection.insert_one(document)

#Print the ID of the inserted document
print('Inserted Document ID:',insert_result.inserted_id)

client.close()