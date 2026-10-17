from PIL import Image
from transformers import pipeline
from WitnessDetails import getInfo
import os


vision_scanner = pipeline(
    task="zero-shot-image-classification", 
    model="google/siglip-so400m-patch14-384"
)


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
               results = vision_scanner(
                   suspect_picture,
                   candidate_labels=required_feature_details,
                   hypothesis_template="a photo of a person with {}."
               )

               current_set = {}
               for feature in results:
                   feature_name = feature['label']
                   confidence = feature['score']
                   if confidence > 0.30:
                       current_set[feature_name] = 1
                   else:
                       current_set[feature_name] = 0

               current_set["image_path"] = image_path 
               array_of_sets.append(current_set)   

            except FileNotFoundError:
                print("This image does not exist in our database")        




    set_of_sets_vs_matches = {}
    set_of_images = {}
             
    for index, suspect_set in enumerate(array_of_sets, start=1):
        match_count = 0
        for feature_truth in suspect_set:
            if feature_truth == "image_path":
                continue
            if suspect_set[feature_truth] == 1:
                 match_count += 1
                 
        set_name = f"set_number_{index}"
        set_of_sets_vs_matches[set_name] = match_count 
        set_of_images[set_name] = suspect_set["image_path"]
        

             
    print(set_of_sets_vs_matches)    
    print("\n")  

    max_val = 0
    
    for set_number in set_of_sets_vs_matches:
        set_match_number = set_of_sets_vs_matches[set_number]
        if set_match_number > max_val:
            max_val = set_match_number


    array_of_priority_options = []
    array_of_priority_images = []

    for set_number in set_of_sets_vs_matches:
        set_match_number = set_of_sets_vs_matches[set_number]     
        if set_match_number == max_val:
            array_of_priority_options.append(set_number)
            array_of_priority_images.append(set_of_images[set_number])

            

    print("\n")
    print("Highest Match: ")
    print(array_of_priority_options)
    print(array_of_priority_images)

         
    


witness_data = getInfo()
print(AI_scanner(witness_data))
