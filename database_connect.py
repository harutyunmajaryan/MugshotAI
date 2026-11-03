from AI_Talking_Agent import speak
from AI_scanner import AI_scanner
from WitnessDetails import getInfo
from PIL import Image
import asyncio
import mysql.connector




connection = mysql.connector.connect(
    host="172.17.128.1", 
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

asyncio.run(speak("Hello, I am your AI assistant. I have found suspects that match your description."))

for row in rows:
    if len(row) > 0:
        try:
          suspect_id = row[0]
          suspect_name = row[1]
          suspect_surname = row[2]
          suspect_age = row[3]
          suspect_address = row[4]
          suspect_image_path = row[5]


          if suspect_image_path in suspect_images_detected:   #if the image path exsits in the priority images then make a query
              
              suspect_query = f"""
                 Suspect Name: {suspect_name}
                 Suspect Surname: {suspect_surname}
                 Suspect Age: {suspect_age}
                 Suspect Home Address: {suspect_address}
                 Suspect Image Path: {suspect_image_path}
                 """
              
              img = Image.open(suspect_image_path)
              img.show()

              message_for_AI = f"Suspect's name is {suspect_name} and surname is {suspect_surname}. {suspect_age} years old, living in {suspect_address}."
              asyncio.run(speak(message_for_AI))  #start speaking
              message_for_AI = ""                 #back to normal


              print(suspect_query)
              print("\n" * 3)

        except (IndexError, FileNotFoundError) as e:
           print(f"Error processing row or image: {e}")  



asyncio.run(speak("Thats all I have Harutyun, thanks for your support and patience."))
cursor.close()
connection.close()



