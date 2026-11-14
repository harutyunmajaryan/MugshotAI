from PIL import Image
from transformers import pipeline
from WitnessDetails import getInfo
import os


vision_scanner = pipeline(
    task="zero-shot-image-classification", 
    model="google/siglip-large-patch16-384"
)


GENDER = [
    "a photo of a man",
    "a photo of a woman",
]

AGE = [
   "a photo of a young adult",
   "a photo of a middle-aged adult",
   "a photo of an elderly person",
]

HAIR_COLOUR = [
    "a photo of a person with black hair",
    "a photo of a person with brown hair",
    "a photo of a person with blonde hair",
    "a photo of a person with red hair",
    "a photo of a person with gray hair",
    "a photo of a person with white hair",
    "a photo of a person with ginger hair",
    "a photo of a person with red hair",
    "a photo of a person with blue hair",
    "a photo of a person with purple hair",
]

HAIR_LENGTH = [
    "a photo of a bald person",
    "a photo of a person with short hair",
    "a photo of a person with medium hair",
    "a photo of a person with long hair",
]

FACIAL_HAIR_TYPE = [
    "a photo of a person with a beard",
    "a photo of a person with a mustache",
    "a photo of a person with a stubble",
    "a clean-shaven face with no facial hair",
]


SKIN_TYPE = [
    "a photo of a person with light skin tone",
    "a photo of a person with dark skin tone",
    "a photo of a person with medium skin tone"
]



MASTER_LABELS = (
  GENDER +
  AGE +
  HAIR_COLOUR +
  HAIR_LENGTH +
  FACIAL_HAIR_TYPE +
  SKIN_TYPE

)



#the function below takes every features of a person and starts scanning them


"""
The function below implements a scanning process for each image in the database by taking the attributes from witness's discription.
It will take simple words like long, blonde, light and many other words, and convert into simple sentence form, so the AI model can understand.
Moreover, the AI model will evaluate the label scores for each feature and try to find the maximum out of them and assign 1 to the feature if the person has that.
If you see 1 in front of a feature that person has it means it is True, and False if you see 0.
Finally, the function will find the sum of truth values for each person from database and check the passing threhold.
If the total number of truth values, for example, 1+1+0+0+1 = 3, passes the threshold = 3 it means, the image path will be attached to an array called priority_images
Otherwise it will skip that person and move on to the next one.
The process will repeat until the last person on database. 
"""

def AI_scanner(witness_provided_data):
    required_feature_details = []
    for data in witness_provided_data:
        required_feature_details.append(witness_provided_data[data]['value'])   
        
    print("\n")
    print("Required features for AI to search: ")
    print(required_feature_details)    
    print("\n")

    array_of_sets = []
    
    for filename in os.listdir("images"):
        if filename.endswith(".png"):
            try:
               image_path = os.path.join("images", filename)
               suspect_picture = Image.open(image_path).convert("RGB")

               current_set = {}

               results = vision_scanner(
                     suspect_picture,
                     candidate_labels=MASTER_LABELS,
                     hypothesis_template="{}"
               )  

               score_map = {res['label']: res['score'] for res in results}

               def return_best_label(category_list):
                  best_label = None
                  highest_score = -1.0
                  for label in category_list:
                        score = score_map.get(label, 0.0)
                        if score > highest_score:
                            highest_score = score
                            best_label = label
                  return best_label

           ###################################################################################################    
              
               if "Gender" in witness_provided_data:
                  witness_gender = witness_provided_data["Gender"]["value"]
                  best_gender = return_best_label(GENDER)

                  if best_gender == witness_gender:
                     current_set[witness_gender] = 1
                  else:
                     current_set[witness_gender] = 0

               ############################################################################
               if "Hair color" in witness_provided_data:
                  witness_hair_colour = witness_provided_data["Hair color"]["value"]
                  best_hair_colour = return_best_label(HAIR_COLOUR)

                  if best_hair_colour == witness_hair_colour:
                     current_set[witness_hair_colour] = 1
                  else:
                     current_set[witness_hair_colour] = 0

              ###############################################################################
               if "Age" in witness_provided_data:
                   witness_age = witness_provided_data["Age"]["value"]
                   best_age = return_best_label(AGE)
              
                   if best_age == witness_age:
                      current_set[witness_age] = 1
                   else:
                      current_set[witness_age] = 0       

              ################################################################################
               if "Hair length" in witness_provided_data:
                  witness_hair_length = witness_provided_data["Hair length"]["value"]
                  best_hair_length = return_best_label(HAIR_LENGTH)

                  if best_hair_length == witness_hair_length:
                     current_set[witness_hair_length] = 1
                  else:
                     current_set[witness_hair_length] = 0

               ##############################################################################
               if "Facial hair" in witness_provided_data:
                  witness_facial_hair_type = witness_provided_data["Facial hair"]["value"]
                  best_facial_hair_type = return_best_label(FACIAL_HAIR_TYPE)

                  if best_facial_hair_type == witness_facial_hair_type:
                     current_set[witness_facial_hair_type] = 1
                  else:
                     current_set[witness_facial_hair_type] = 0

               #########################################################################################
            
               if "Skin colour" in witness_provided_data:
                  witness_skin_colour = witness_provided_data["Skin colour"]["value"]
                  best_skin_colour = return_best_label(SKIN_TYPE)

                  if best_skin_colour == witness_skin_colour:
                     current_set[witness_skin_colour] = 1
                  else:
                     current_set[witness_skin_colour] = 0  
                #####################################################################      
                      
                 #array_of_sets = [{feature_name1 : 1, feature_name2 : 0, image_path: "...."}, {.......}]

               current_set["image_path"] = image_path 
               array_of_sets.append(current_set)
               print(current_set)
               print("\n")
            

            except FileNotFoundError:
                print("This image does not exist in our database")     



    print("\n" * 2)
    suspect_vs_matches = {}

    for suspect_set in array_of_sets:
        match_score = 0
        for feature_truth in suspect_set:
            if suspect_set[feature_truth] == 1:
                match_score += 1
            elif suspect_set[feature_truth] == 0:
                match_score += 0    
            elif feature_truth == "image_path":
                continue  

        suspect_vs_matches[suspect_set["image_path"]] = match_score

    print(suspect_vs_matches)     


    priority_images = []
    return_threshold = 3

    for image_path_for_match in suspect_vs_matches:
        if suspect_vs_matches[image_path_for_match] >= return_threshold:     #suspect_vs_matches[image_path_for_match] is match_score for each image > threshold
            priority_images.append(image_path_for_match)                    #priortiy_images is the array that contains all the image paths which exceeded the threshold

    return priority_images

                 
