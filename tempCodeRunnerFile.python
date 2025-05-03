import pymongo

try:
    client = pymongo.MongoClient("mongodb+srv://abhijeetsri11:Meatwork@heisenberg.m6sn61k.mongodb.net/?retryWrites=true&w=majority", serverSelectionTimeoutMS=3000)
    client.admin.command('ping')
    print("✅ MongoDB is connected!")
except Exception as e:
    print("❌ MongoDB connection failed:", e)
