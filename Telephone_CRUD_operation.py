"""
@author: mogit
"""
"""Creating a sample database using pymongo with telephone directory details 
and performing CRUD operations on the data"""
import pymongo

mongo=pymongo.MongoClient("mongodb://127.0.0.1:27017/") #mongo client was imported

Tele=mongo['Telephone_Directory'] #created a mongo database using Tele as pointer
directory=Tele['Directory'] # created collection inside Telephone_Directory 

# data to be inserted
contactinfo1={'name':'ram',
    'phoneno':9902930746,
              'email':'firstmail@gmail.com',
              'address':'69,cross street, DB nagar'           
    }
contactinfo2={'name':'raj',
    'phoneno':98349756361,
              'email':'secondmail@gmail.com',
              'address':'33444,straight street, sl nagar'           
    }
directory.insert_one(contactinfo1) #used insert_one function to insert one document
directory.insert_one(contactinfo2)
userinfomany=[
    {'name':'john','phoneno':78763242428,'address':'2-main road NY south'},
    {'name':'james','phoneno':876457478,'email':'vardy29@yahoo.com'},
    {'name':'abdul','phoneno':8364777390}
    ]

directory.insert_many(userinfomany) #used insert_many function to insert many documents 
data=directory.find({},{})
for d in data:
    print(d)
"""output for the code
{'_id': ObjectId('635e4792117c45449e01519d'), 'name': 'ram', 'phoneno': 9902930746, 'email': 'firstmail@gmail.com', 'address': '69,cross street, DB nagar'}
{'_id': ObjectId('635e47e6117c45449e01519f'), 'name': 'raj', 'phoneno': 98349756361, 'email': 'secondmail@gmail.com', 'address': '33444,straight street, sl nagar'}
{'_id': ObjectId('635e490a117c45449e0151a1'), 'name': 'john', 'phoneno': 78763242428, 'address': '2-main road NY south'}
{'_id': ObjectId('635e490a117c45449e0151a2'), 'name': 'james', 'phoneno': 876457478, 'email': 'vardy29@yahoo.com'}
{'_id': ObjectId('635e490a117c45449e0151a3'), 'name': 'abdul', 'phoneno': 8364777390}
"""
data1=directory.find({'name':'john'},{'_id':0}) #querying data for user john
for d in data1:
    print(d)
    
"""output for this CMD =
{'name': 'john', 
 'phoneno': 78763242428, 
 'address': '2-main road NY south'}"""

#performing update operation in dataset
query={'name':'abdul'} 
update={'$set':{'address':'12 baker street london'}}

directory.update_one(query,update) #updating the document with address field , whereas previously it's not inserted
"""output for the CMD =
{'_id': ObjectId('635e490a117c45449e0151a3'),
 'name': 'abdul', 'phoneno': 8364777390, 
 'address': '12 baker street london'}"""

#performing Delete operation in dataset
directory.delete_one({'name':'john'}) #deleting document which contains john in name field

""" output for the CMD =
{
        "_id" : ObjectId("635e4792117c45449e01519d"),
        "name" : "ram",
        "phoneno" : NumberLong("9902930746"),
        "email" : "firstmail@gmail.com",
        "address" : "69,cross street, DB nagar"
}
{
        "_id" : ObjectId("635e47e6117c45449e01519f"),
        "name" : "raj",
        "phoneno" : NumberLong("98349756361"),
        "email" : "secondmail@gmail.com",
        "address" : "33444,straight street, sl nagar"
}
{
        "_id" : ObjectId("635e490a117c45449e0151a2"),
        "name" : "james",
        "phoneno" : 876457478,
        "email" : "vardy29@yahoo.com"
}
{
        "_id" : ObjectId("635e490a117c45449e0151a3"),
        "name" : "abdul",
        "phoneno" : NumberLong("8364777390"),
        "address" : "12 baker street london"
}















