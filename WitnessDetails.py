from typing import Callable

def getInfo() -> dict[str, str | int]:
    print("Fill the suspect's details below:\n")

    map = {}
    threshold = 70

    AVAILABLE_COLOURS = ["blonde", "black", "brown", "red", "gray", "white", "ginger", "blue", "pink", "purple"]
    AVAILABLE_LENGTHS = ["long", "short", "medium"]
    AVAILABLE_FACIAL_HAIR = ["beard", "mustache", "stubble"]
    AVAILABLE_SKIN_TONES = ["light", "dark", "medium"]

    
    """
    This is the questioniare part, where we take all the data from witnesses. 
    All questions must be derived from another relevent question. For example, if we take a data about hair every single question that is related to hari must be derived from one to another one.
    All the TypeError and ValueError cases must be handled properly. 
    Sureness scores must be between 0 and 100, which means they must be natural integers.
    """

    #The inputs should take while loop so whenever the customer makes mistakes or typos the program will shot down immidietly which is not the best way to handle this issue.!!!!!!!!!!    

    # 1. Suspect Gender
    def gender_reveal() -> dict[str, str | int]:
        gender = input("Is your person male?(yes/no): ").strip().lower()
        if gender in ["yes", "no"]:
            if gender == "yes":  
              gender_score = int(input("How sure are you on a scale from 0 to 100?: "))
              if (threshold <= gender_score <= 100):
                  map["Gender"] = {"value": "a photo of a man", "score": gender_score}
              elif gender_score < 0 or gender_score > 100:
                  raise ValueError("The score cannot be outside the range!")
              elif (0 <= gender_score < threshold):
                  pass
            elif gender == "no":
               gender_score = int(input("How sure are you on a scale from 0 to 100?: "))
               if (threshold <= gender_score <= 100):
                   map["Gender"] = {"value": "a photo of a woman", "score": gender_score}
               elif gender_score < 0 or gender_score > 100:
                   raise ValueError("The score cannot be outside the range!")
               elif (0 <= gender_score < threshold):
                   pass
        elif gender not in ["yes","no"] or gender == "":
            return f"{gender} cannot be passed to the model!"
        return map     


    def age_reveal() -> dict[str, str | int]:
        age = input("How old coule the person be?: (skip if you dont know): ").strip()
        if age == "skip":
            pass
        elif (18 <= int(age) <= 29):
            age_score = int(input("How sure are you on a scale from 0 to 100?: "))
            if (threshold <= age_score <= 100):
                map["Age"] = {"value": "a photo of a young adult", "score": age_score}
            elif age_score > 100 or age_score < 0:
                raise ValueError("The score cannot be outside the range!")
            elif (0 <= age_score < threshold):
                pass

        elif (30 <= int(age) <= 59):
             age_score = int(input("How sure are you on a scale from 0 to 100?: "))
             if (threshold <= age_score <= 100):
                map["Age"] = {"value": "a photo of a middle-aged adult", "score": age_score}
             elif age_score > 100 or age_score < 0:  
                raise ValueError("The score cannot be outside the range!")
             elif (0 <= age_score < threshold):
                pass       

        elif (60 <= int(age) <= 120):
            age_score = int(input("How sure are you on a scale from 0 to 100?: "))
            if (threshold <= age_score <= 100):
                map["Age"] = {"value": "a photo of an elderly person", "score": age_score}
            elif age_score > 100 or age_score < 0:  
                raise ValueError("The score cannot be outside the range!")
            elif (0 <= age_score < threshold):
                pass  

        elif int(age) < 0 or int(age) > 120:
            raise ValueError("The age does not make sense!")
        
        return map          


    def hair_length_reveal() -> dict[str, str | int]:
        hair_length = input("How long was the hair? (long/medium/short/bald): ").strip().lower()
        if hair_length in AVAILABLE_LENGTHS:
            hair_length_score = int(input("How sure are you on a scale from 0 to 100?: "))
            if (threshold <= hair_length_score <= 100):
                map["Hair length"] = {"value": f"a photo of a person with {hair_length} hair", "score": hair_length_score}
            elif hair_length_score > 100 or hair_length_score < 0:
                raise ValueError("The score cannot be outside the range!")
            elif (0 <= hair_length_score < threshold):
                pass
        elif hair_length == "bald":
            hair_length_score = int(input("How sure are you on a scale from 0 to 100?: "))
            if (threshold <= hair_length_score <= 100):
                map["Hair length"] = {"value": "a photo of a bald person", "score": hair_length_score}
            elif hair_length_score > 100 or hair_length_score < 0:
                raise ValueError("The score cannot be outside the range!")
            elif (0 <= hair_length_score < threshold):
                pass
    
        elif hair_length not in AVAILABLE_LENGTHS or hair_length == "":
            raise TypeError("The inserted length do not match!")
        return map

    
    def hair_colour_reveal() -> dict[str, str | int]:
        hair_colour = input("What colour was the hair? (please insert colour or skip the question): ").strip().lower()
        if hair_colour == "skip":
            pass
        elif hair_colour in AVAILABLE_COLOURS:
            hair_colour_score = int(input("How sure are you on a scale from 0 to 100?: "))
            if (threshold <= hair_colour_score <= 100):
                map["Hair color"] = {"value": f"a photo of a person with {hair_colour} hair", "score": hair_colour_score} 
            elif hair_colour_score < 0 or hair_colour_score > 100:
                raise ValueError("The score cannot be outside the range!")
            elif (0 <= hair_colour_score < threshold):
                pass
        elif hair_colour not in AVAILABLE_COLOURS or hair_colour == "":
            raise TypeError("The inserted colour do not match!")
        return map                 



    def facial_hair_reveal() -> dict[str, str | int]:
        facial_hair = input("What type of facial hair did your person have? (beard/mustache/stubble/no(otherwise)): ").strip().lower()
        if facial_hair in AVAILABLE_FACIAL_HAIR:
            facial_hair_score = int(input("How sure are you on a scale from 0 to 100?: "))
            if (threshold <= facial_hair_score <= 100):
                map["Facial hair"] = {"value": f"a photo of a person with a {facial_hair}", "score": facial_hair_score}
            elif facial_hair_score < 0 or facial_hair_score > 100:
                raise ValueError("The score cannot be outside the range!")
            elif (0 <= facial_hair_score < threshold):
                pass

        elif facial_hair == "no":
            facial_hair_score = int(input("How sure are you on a scale from 0 ot 100?: "))
            if (threshold <= facial_hair_score <= 100):
                map["Facial hair"] = {"value": "a clean-shaven face with no facial hair", "score": facial_hair_score}
            elif facial_hair_score < 0 or facial_hair_score > 100:
                raise ValueError("The score cannot be outside the range!")
            elif (0 <= facial_hair_score < threshold):
                pass

        elif facial_hair not in AVAILABLE_FACIAL_HAIR or facial_hair == "":
            raise TypeError("The inserted facial hair do not match!")
        return map


    def  skin_type_reveal() -> dict[str, str | int]:
        skin_type = input("What type of skin did you person have? (light, medium, dark)?: ").strip().lower()
        if skin_type in AVAILABLE_SKIN_TONES:
            skin_type_score = int(input("How sure are you on a scale from 0 to 100?: "))
            if (threshold <= skin_type_score <= 100):
                map["Skin colour"] = {"value": f"a photo of a person with {skin_type} skin tone", "score": skin_type_score}
            elif skin_type_score > 100 or skin_type_score < 0:
                raise ValueError("The score cannot be outside the range!")
            elif (0 <= skin_type_score < threshold): 
                pass
        elif skin_type not in AVAILABLE_SKIN_TONES or skin_type == "":
            raise TypeError("The inserted skin type do not match!")
        return map      


    gender_reveal()
    age_reveal()
    hair_length_reveal()
    hair_colour_reveal()
    facial_hair_reveal()
    skin_type_reveal()
    

    print("\n==============================")
    print("FINAL COMPILED MAP:")
    print("==============================")
    print(map)
    
    return map

if __name__ == "__main__":
    final_result = getInfo()

   


     
