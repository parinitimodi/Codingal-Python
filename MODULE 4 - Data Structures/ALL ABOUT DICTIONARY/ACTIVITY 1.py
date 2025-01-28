student_data = {"id1":
                {"name":["Vamshi"],
                 "class":["6D"],
                 "subjectintegration":["English"],
                },
                "id2":
                 {"name":["Pariniti"],
                 "class":["6E"],
                 "subjectintegration":["English"],
                 
                 },
                "id3":
                 {"name":["Vihani"],
                 "class":["6E"],
                 "subjectintegration":["English"],
                 },
                "id4":
                 {"name":["Rohit"],
                 "class":["7G"],
                 "subjectintegration":["English"],
                },
                "id5":
                 {"name":["Vamshi"],
                 "class":["6D"],
                 "subjectintegration":["English"],
                },
                }
result = {}
for key,value in student_data.items():
    if value not in result.values():
        result [key] = value

print (result)

                