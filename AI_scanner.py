from PIL import Image
from transformers import pipeline
from WitnessDetails import getInfo
import os


vision_scanner = pipeline(
    task="zero-shot-image-classification", 
    model="google/siglip-large-patch16-384"
)


GENDER = [
    "a photo of a man.",
    "a photo of a woman.",
]

HAIR_COLOUR = [
    "a photo of a person with black hair.",
    "a photo of a person with brown hair.",
    "a photo of a person with blonde hair.",
    "a photo of a person with red hair.",
    "a photo of a person with gray hair.",
]

HAIR_LENGTH = [
    "a photo of a bald person.",
    "a photo of a person with short hair.",
    "a photo of a person with medium hair.",
    "a photo of a person with long hair.",
]

FACIAL_HAIR_TYPE = [
    "a photo of a person with a beard.",
    "a photo of a person with a mustache.",
    "a photo of a person with stubble.",
    "a photo of a clean-shaven person.",
]

FACIAL_HAIR_COLOUR = [
    "a photo of a person with a black beard.",
    "a photo of a person with a brown beard.",
    "a photo of a person with a blonde beard.",
    "a photo of a person with a red beard.",
    "a photo of a person with a gray beard.",
    "a photo of a person with a black mustache.",
    "a photo of a person with a brown mustache.",
    "a photo of a person with a blonde mustache.",
    "a photo of a person with a red mustache.",
    "a photo of a person with a gray mustache.",
    "a photo of a person with black stubble.",
    "a photo of a person with brown stubble.",
    "a photo of a person with blonde stubble.",
    "a photo of a person with red stubble.",
    "a photo of a person with gray stubble.",
]

FACIAL_HAIR_LENGTH = [
    "a photo of a person with a short beard.",
    "a photo of a person with a medium beard.",
    "a photo of a person with a long beard.",
]

SKIN_TYPE = [
    "a photo of a person with light skin.",
    "a photo of a person with dark skin.",
]


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


           ###################################################################################################    
              
               if "Gender" in witness_provided_data:
                  witness_gender = witness_provided_data["Gender"]["value"]

                  results = vision_scanner(
                     suspect_picture,
                     candidate_labels=GENDER,
                     hypothesis_template="{}"
                  )

                  set_of_values_for_gender = {}
                  for feature in results:
                     set_of_values_for_gender[feature['label']] = feature['score']

                  maximum_value_for_gender = 0
                  final_decision_of_gender = None
                  for maximum in set_of_values_for_gender:
                     if set_of_values_for_gender[maximum] > maximum_value_for_gender:
                        maximum_value_for_gender = set_of_values_for_gender[maximum]
                        final_decision_of_gender = maximum

                  if final_decision_of_gender == witness_gender:
                     current_set[witness_gender] = 1
                  else:
                     current_set[witness_gender] = 0


               ############################################################################
               if "Hair color" in witness_provided_data:
                  witness_hair_colour = witness_provided_data["Hair color"]["value"]

                  results = vision_scanner(
                     suspect_picture,
                     candidate_labels=HAIR_COLOUR,
                     hypothesis_template="{}"
                  )

                  set_of_values_for_hair_colour = {}
                  for feature in results:
                     set_of_values_for_hair_colour[feature['label']] = feature['score']

                  maximum_value_for_hair_colour = 0
                  final_decision_of_hair_colour = None
                  for maximum in set_of_values_for_hair_colour:
                     if set_of_values_for_hair_colour[maximum] > maximum_value_for_hair_colour:
                        maximum_value_for_hair_colour = set_of_values_for_hair_colour[maximum]
                        final_decision_of_hair_colour = maximum

                  if final_decision_of_hair_colour == witness_hair_colour:
                     current_set[witness_hair_colour] = 1
                  else:
                     current_set[witness_hair_colour] = 0


              ################################################################################
               if "Hair length" in witness_provided_data:
                  witness_hair_length = witness_provided_data["Hair length"]["value"]

                  results = vision_scanner(
                     suspect_picture,
                     candidate_labels=HAIR_LENGTH,
                     hypothesis_template="{}"
                  )

                  set_of_values_for_hair_length = {}
                  for feature in results:
                     set_of_values_for_hair_length[feature['label']] = feature['score']

                  maximum_value_for_hair_length = 0
                  final_decision_of_hair_length = None
                  for maximum in set_of_values_for_hair_length:
                     if set_of_values_for_hair_length[maximum] > maximum_value_for_hair_length:
                        maximum_value_for_hair_length = set_of_values_for_hair_length[maximum]
                        final_decision_of_hair_length = maximum

                  if final_decision_of_hair_length == witness_hair_length:
                     current_set[witness_hair_length] = 1
                  else:
                     current_set[witness_hair_length] = 0


               ##############################################################################
               if "Facial hair" in witness_provided_data:
                  witness_facial_hair_type = witness_provided_data["Facial hair"]["value"]

                  results = vision_scanner(
                     suspect_picture,
                     candidate_labels=FACIAL_HAIR_TYPE,
                     hypothesis_template="{}"
                  )

                  set_of_values_for_facial_hair_type = {}
                  for feature in results:
                     set_of_values_for_facial_hair_type[feature['label']] = feature['score']

                  maximum_value_for_facial_hair_type = 0
                  final_decision_of_facial_hair_type = None
                  for maximum in set_of_values_for_facial_hair_type:
                     if set_of_values_for_facial_hair_type[maximum] > maximum_value_for_facial_hair_type:
                        maximum_value_for_facial_hair_type = set_of_values_for_facial_hair_type[maximum]
                        final_decision_of_facial_hair_type = maximum

                  if final_decision_of_facial_hair_type == witness_facial_hair_type:
                     current_set[witness_facial_hair_type] = 1
                  else:
                     current_set[witness_facial_hair_type] = 0


               #########################################################################################
               if "Facial hair colour" in witness_provided_data:
                  witness_facial_hair_colour = witness_provided_data["Facial hair colour"]["value"]

                  results = vision_scanner(
                     suspect_picture,
                     candidate_labels=FACIAL_HAIR_COLOUR,
                     hypothesis_template="{}"
                  )

                  set_of_values_for_facial_hair_colour = {}
                  for feature in results:
                     set_of_values_for_facial_hair_colour[feature['label']] = feature['score']

                  maximum_value_for_facial_hair_colour = 0
                  final_decision_of_facial_hair_colour = None
                  for maximum in set_of_values_for_facial_hair_colour:
                     if set_of_values_for_facial_hair_colour[maximum] > maximum_value_for_facial_hair_colour:
                        maximum_value_for_facial_hair_colour = set_of_values_for_facial_hair_colour[maximum]
                        final_decision_of_facial_hair_colour = maximum

                  if final_decision_of_facial_hair_colour == witness_facial_hair_colour:
                     current_set[witness_facial_hair_colour] = 1
                  else:
                     current_set[witness_facial_hair_colour] = 0


               #######################################################################
               if "Beard length" in witness_provided_data:
                  witness_beard_length = witness_provided_data["Beard length"]["value"]

                  results = vision_scanner(
                     suspect_picture,
                     candidate_labels=FACIAL_HAIR_LENGTH,
                     hypothesis_template="{}"
                  )

                  set_of_values_for_beard_length = {}
                  for feature in results:
                     set_of_values_for_beard_length[feature['label']] = feature['score']

                  maximum_value_for_beard_length = 0
                  final_decision_of_beard_length = None
                  for maximum in set_of_values_for_beard_length:
                     if set_of_values_for_beard_length[maximum] > maximum_value_for_beard_length:
                        maximum_value_for_beard_length = set_of_values_for_beard_length[maximum]
                        final_decision_of_beard_length = maximum

                  if final_decision_of_beard_length == witness_beard_length:
                     current_set[witness_beard_length] = 1
                  else:
                     current_set[witness_beard_length] = 0


               ###############################################################
               if "Skin colour" in witness_provided_data:
                  witness_skin_colour = witness_provided_data["Skin colour"]["value"]

                  results = vision_scanner(
                     suspect_picture,
                     candidate_labels=SKIN_TYPE,
                     hypothesis_template="{}"
                  )

                  set_of_values_for_skin_colour = {}
                  for feature in results:
                     set_of_values_for_skin_colour[feature['label']] = feature['score']

                  maximum_value_for_skin_colour = 0
                  final_decision_of_skin_colour = None
                  for maximum in set_of_values_for_skin_colour:
                     if set_of_values_for_skin_colour[maximum] > maximum_value_for_skin_colour:
                        maximum_value_for_skin_colour = set_of_values_for_skin_colour[maximum]
                        final_decision_of_skin_colour = maximum

                  if final_decision_of_skin_colour == witness_skin_colour:
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

            


         
