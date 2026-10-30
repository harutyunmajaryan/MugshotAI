import mysql.connector
from AI_scanner import AI_scanner
from WitnessDetails import getInfo
from PIL import Image



connection = mysql.connector.connect(
    host="***.**.***.*", 
    user="root",
    password="", 
    port=3308,    
    database="JJ", 
)


cursor = connection.cursor()
query = """
    SELECT 
        SUSPECTS.id,
        SUSPECTS.suspect_name,
        SUSPECTS.suspect_surname,
        SUSPECTS.age,
        SUSPECTS.suspect_address,
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
    if len(row) > 0:
        try:
          suspect_id = row[0]
          suspect_name = row[1]
          suspect_surname = row[2]
          suspect_age = row[3]
          suspect_address = row[4]
          suspect_image_path = row[5]

          for image_path in suspect_images_detected:
            if image_path == suspect_image_path:

              suspect_query = f"""
                 Suspect Name: {suspect_name}
                 Suspect Surname: {suspect_surname}
                 Suspect Age: {suspect_age}
                 Suspect Home Address: {suspect_address}
                 Suspect Image Path: {suspect_image_path}
                 """
              img = Image.open(image_path)
              img.show()
            

              print(suspect_query)
              print("\n" * 3)

        except (IndexError, FileNotFoundError) as e:
           print(f"Error processing row or image: {e}")  


cursor.close()
connection.close()

#closing cursor and connection after processing everything


