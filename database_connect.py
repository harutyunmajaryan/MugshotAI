import mysql.connector
from AI_scanner import AI_scanner
from WitnessDetails import getInfo
from PIL import Image


connection = mysql.connector.connect(
    host="************", 
    user="root",
    password="", 
    port="****",  
    database="JJ",  
)


cursor = connection.cursor()
query = """
    SELECT 
        SUSPECTS.id,
        SUSPECTS.suspect_name,
        SUSPECTS.suspect_surname,
        SUSPECTS.age,
        SUSPECT_IMAGE_TABLE.image_path
    FROM SUSPECT_IMAGE_TABLE
    JOIN SUSPECTS 
      ON SUSPECTS.suspect_name = SUSPECT_IMAGE_TABLE.suspect_name 
     AND SUSPECTS.suspect_surname = SUSPECT_IMAGE_TABLE.suspect_surname;
"""

cursor.execute(query)
rows = cursor.fetchall()

print("AI is scanning ...")
suspect_images_detected = AI_scanner(getInfo())  #this is the array of all images of suspects 


for row in rows:
    suspect_id = row[0]
    suspect_name = row[1]
    suspect_surname = row[2]
    suspect_age = row[3]
    suspect_image_path = row[4]

    for image_path in suspect_images_detected:
        if image_path == suspect_image_path:

            suspect_query = f"""
            Suspect Name: {suspect_name}
            Suspect Surname: {suspect_surname}
            Suspect Age: {suspect_age}
            """

            print(suspect_query)

            img = Image.open(f"{suspect_image_path}")
            img.show()
            print("\n" * 3)
            
