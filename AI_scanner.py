from PIL import Image
from transformers import pipeline
from WitnessDetails import getInfo
import os


vision_scanner = pipeline(
    task="zero-shot-image-classification", 
    model="google/siglip-large-patch16-384"
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
               print(current_set)  

               #array_of_sets = [{feature_name1 : 1, feature_name2 : 0, image_path: "...."}, {.......}]

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
    return_threshold = 2

    for image_path_for_match in suspect_vs_matches:
        if suspect_vs_matches[image_path_for_match] >= return_threshold:     #suspect_vs_matches[image_path_for_match] is match_score for each image > threshold
            priority_images.append(image_path_for_match)                    #priortiy_images is the array that contains all the image paths which exceeded the threshold

    print(priority_images)
    return priority_images

            


         
