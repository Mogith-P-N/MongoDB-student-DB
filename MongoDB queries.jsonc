# Json file was exported into the MongoDB using Mongocompass GUI and collections were created with name ExamReports
# To find the database schema and read the type of data
db.ExamReports.find().pretty()

# 1)Find the student name who scored maximum scores in all (exam, quiz and homework)?

db.ExamReports.find({"scores.0.score":{$gte:90},"scores.1.score":{$gte:90},"scores.2.score":{$gte:90}})
 # ANS : { "_id" : 13, "name" : "Jessika Dagenais", "scores" : [ { "score" : 90.47179954427436, "type" : "exam" }, { "score" : 90.3001402468489, "type" : "quiz" }, { "score" : 95.17753772405909, "type" : "homework" } ] }

# 2) Find students who scored below average in the exam and pass mark is 40%? (typically considering 60 as avg )

db.ExamReports.find({"scores.0.score":{$lte:60}})
# result - 120 documents were found and stored in separate collection "StudentGuvi.belowAvginExam".

# 3) Find students who scored below pass mark and assigned them as fail, and above pass mark as pass in all the categories

db.ExamReports.updateMany({},
... {$set: {"scores.$[elem].result":"Pass"}},
... {arrayFilters:[{"elem.score":{$gte:40}}]})

db.ExamReports.updateMany({},
... {$set: {"scores.$[elem].result":"Fail"}},
... {arrayFilters:[{"elem.score":{$lt:40}}]})

# result - updated all the documents satisfied these conditions. sample results from queries
"""
     "_id" : 18,
        "name" : "Verdell Sowinski",
        "scores" : [
                {
                        "score" : 62.12870233109035,
                        "type" : "exam",
                        "result" : "Pass"
                },
                {
                        "score" : 84.74586220889356,
                        "type" : "quiz",
                        "result" : "Pass"
                },
                {
                        "score" : 81.58947824932574,
                        "type" : "homework",
                        "result" : "Pass"
                }
        ]
}
{
        "_id" : 19,
        "name" : "Gisela Levin",
        "scores" : [
                {
                        "score" : 44.51211101958831,
                        "type" : "exam",
                        "result" : "Pass"
                },
                {
                        "score" : 0.6578497966368002,
                        "type" : "quiz",
                        "result" : "Fail"
                },
                {
                        "score" : 93.36341655949683,
                        "type" : "homework",
                        "result" : "Pass"
                    
                }    
        ]
}
"""
            

# 4) Find the total and average of the exam, quiz and homework and store them in a separate collection.
# Method-1 to find cumulative sum and avg for all the students based on category type (Exam, quiz and homework)

db.ExamReports.aggregate([{$unwind:{path:"$scores"}},{$group:{_id:"$scores.type",Totalsum:{$sum:"$scores.score"},Avgscore:{$avg:"$scores.score"}}}])

# result for the above query
"""
{ "_id" : "exam", "Totalsum" : 9734.734151900351, "Avgscore" : 48.67367075950175 }
{ "_id" : "quiz", "Totalsum" : 9799.344638860508, "Avgscore" : 48.99672319430254 }
{ "_id" : "homework", "Totalsum" : 13563.739241322297, "Avgscore" : 67.81869620661149 }

"""
# Method-2
# To find total sum and avg of exam, quiz and homework for each students.

db.ExamReports.aggregate([{"$addFields":{"TotalScore":{"$sum":"$scores.score"}}},
... {"$addFields":{"AvgScore":{"$avg":"$scores.score"}}}])

# Sample results for above query . Results were stored in separate collection "StudentGuvi.AvgandTotalscores"
"""
 { "_id" : 0,
  "name" : "aimee Zank", 
 "scores" : [
     { "score" : 1.463179736705023, "type" : "exam", "result" : "Fail" }, 
     { "score" : 11.78273309957772, "type" : "quiz", "result" : "Fail" }, 
     { "score" : 35.8740349954354, "type" : "homework", "result" : "Fail" } ], 
     "TotalScore" : 49.11994783171814,
      "AvgScore" : 16.373315943906046 }

{ "_id" : 1,
 "name" : "Aurelia Menendez",
  "scores" :
   [ { "score" : 60.06045071030959, "type" : "exam", "result" : "Pass" },
    { "score" : 52.79790691903873, "type" : "quiz", "result" : "Pass" },
     { "score" : 71.76133439165544, "type" : "homework", "result" : "Pass" } ],
      "TotalScore" : 184.61969202100374, 
      "AvgScore" : 61.53989734033458 }
      
"""
# 5)  Create a new collection which consists of students who scored below average and above 40% in all the categories.

db.ExamReports.find({$or:[{"scores.0.score":{$gte:40,$lte:60}},
{"scores.1.score":{$lte:60,$gte:40}},
{"scores.2.score":{$lte:60, $gte:40}}]})

# result - 93 records came as a result of the query and stored it into new collection "StudentGuvi.Scoreaobve40below60"

# 6) Create a new collection which consists of students who scored below the fail mark in all the categories.

db.ExamReports.find({"scores.0.score":{$lt:40},"scores.1.score":{$lt:40},"scores.2.score":{$lt:40}})

#result - 1 student were found to be failed in all categories and result was stored in new collection "StudentGuvi.scorebelow40"
"""
{
        "_id" : 0,
        "name" : "aimee Zank",
        "scores" : [
                {
                        "score" : 1.463179736705023,
                        "type" : "exam"
                },
                {
                        "score" : 11.78273309957772,
                        "type" : "quiz"
                },
                {
                        "score" : 35.8740349954354,
                        "type" : "homework"
                }
        ]
}
"""
# 7) Create a new collection which consists of students who scored above pass mark in all the categories.

db.ExamReports.find({"scores.0.score":{$gte:40},"scores.1.score":{$gte:40},"scores.2.score":{$gte:40}})

# result - 54 records were found and stored in new collection " StudentGuvi.Scoreabove40"

