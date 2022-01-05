from ClassDao import student_xDAO

# Create
latestId = student_xDAO.createTable(('mark', 45))

#find by id
result = student_xDAO.findByID(latestId);
print(result)

#update
student_xDAO.updateTable(('Fred', 21, latestId))
result = student_xDAO.findByID(latestId);
print(result)

#get all
allStudents = student_xDAO.getAll()
for student in allStudents:
    print(student)
    
# delete
student_xDAO.deleteRecord(latestId)