import csv
import pymysql
# filename = "Criminal_count.csv"
# num=0
# with open(filename, 'w') as csvfile:
#     csvwriter = csv.writer(csvfile)
#     csvwriter.writerow([5])
def insertData(data):
    field=['Name', "Father's Name", "Gender", "DOB","Crimes"]
    x=[data['Name'], data["Father's Name"], data['Gender'], data['DOB(yyyy-mm-dd)'], data['Crimes Done']]
    filen = "Criminal.csv"
    with open(filen, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(field)
        csvwriter.writerow(x)
        
        
def retrieveData(name):
    id = None
    crim_data = None

    db = pymysql.connect('localhost')
    cursor = db.cursor()
    print("database connected")

    query = "SELECT * FROM criminaldata WHERE name='%s'"%name

    try:
        cursor.execute(query)
        result = cursor.fetchone()

        id=result[0]
        crim_data = {
            "Name" : result[1],
            "Father's Name" : result[2],
            "Mother's Name" : result[3],
            "Gender" : result[4],
            "DOB(yyyy-mm-dd)" : result[5],
            "Blood Group" : result[6],
            "Identification Mark" : result[7],
            "Nationality" : result[8],
            "Religion" : result[9],
            "Crimes Done" : result[10]
        }

        print("data retrieved")
    except:
        print("Error: Unable to fetch data")

    db.close()
    print("connection closed")

    return (id, crim_data)        
        
'''
 def insertData(data):
     print(data['Name'])
     rowId=0
     db=sqlite3.connect('profile.db')
     cursor=db.cursor()
     print("Opened Database")
     query = "INSERT INTO criminaldata VALUES(NAME,FATHER NAME, GENDER, DOB, CRIMES);" % \
             (data['Name'], data["Father's Name"], data['Gender'],
              data['DOB(yyyy-mm-dd)'], data['Crimes Done'])
     cursor.execute(query)
     db.commit()
     rowId=cursor.lastrowid
     print("RowId %d" % rowId)
     print("Record Created")
     db.close()
     return rowId
 def insertData(data):
     # print(data)
 	rowId = 0
 	db = sqlite3.connect('test.db')
     cursor = db.cursor()
     # cursor=db.cursor()
 	print("Opened database Succesfully")
 	query = "INSERT INTO criminaldata VALUES(0, '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s', '%s');" % \
             (data["Name"], data["Father's Name"], data["Mother's Name"], data["Gender"],
              data["DOB(yyyy-mm-dd)"], data["Blood Group"], data["Identification Mark"],
              data["Nationality"], data["Religion"], data["Crimes Done"])
     cursor.execute(query)
     db.commit()
     rowId = cursor.lastrowid
     print("data stored on row %d" % rowId)
     db.commit()
 	print ("Records created successfully");
 	db.close()
 	return rowId
'''