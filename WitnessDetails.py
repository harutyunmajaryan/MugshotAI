def getInfo():
    print("Fill the suspect's details below:\n")

    map = {}
    threshold = 70

    # 1. Suspect Gender
    suspect_gender = input("Is your person male? (yes/no): ").strip().lower()
    if suspect_gender == "yes":
        gender_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
        if gender_sureness >= threshold:
            map["Gender"] = {"value": "male", "sureness": gender_sureness}
    else:
        gender_sureness = int(input("How sure are you that your person is female on a scale from 0 to 100?: "))
        if gender_sureness >= threshold:
            map["Gender"] = {"value": "female", "sureness": gender_sureness}

    # 2. Suspect Hair Availability
    suspect_hair = input("Does your person have hair? (yes/no/idk): ").strip().lower()
    if suspect_hair == "yes":
        suspect_hair_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
        if suspect_hair_sureness >= threshold:
            suspect_hair_colour = input("What colour is the hair? (idk/colour): ").strip().lower()
            if suspect_hair_colour != "idk":
                    suspect_hair_colour_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
                    if suspect_hair_colour_sureness >= threshold:
                        suspect_hair_length = str(input("How long is the hair? (short/medium/long/idk): "))
                        if suspect_hair_length != "idk":
                          map["Hair color"] = {"value": suspect_hair_length + " " + suspect_hair_colour + " " + "hair", "sureness": suspect_hair_colour_sureness}
                        elif suspect_hair_length == "idk":
                          map["Hair color"] = {"value": suspect_hair_colour + " " + "hair", "sureness": suspect_hair_colour_sureness}
                    elif suspect_hair_colour_sureness < threshold:
                          map["Hair color"] = {"value": "hair", "sureness": suspect_hair_colour_sureness}


    elif suspect_hair == "no":
        hair_sureness = int(input("How sure are you that they have no hair/are bald? (0-100): "))
        if hair_sureness >= threshold:
            map["Hair"] = {"value": "bald", "sureness": hair_sureness}

    # 3. Suspect Hair Color
    
    # 4. Suspect Eye Color (Fixed the variable bug here)
    suspect_eye_colour = input("What colour of eyes does your person have? (color/idk): ").strip().lower()
    if suspect_eye_colour != "idk":
        suspect_eye_colour_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
        if suspect_eye_colour_sureness >= threshold:
            suspect_eye_shape = str(input("What shape do the eyes have?(round/narrow/wide/idk): ")).strip().lower()
            if suspect_eye_shape == "idk":
              map["Eye color"] = {"value": suspect_eye_colour + " " + "eyes", "sureness": suspect_eye_colour_sureness}
            else:
                suspect_eye_shape_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
                if suspect_eye_colour_sureness >= threshold:
                    map["Eye color"] = {"value": suspect_eye_shape + " " + suspect_eye_colour + " " + "eyes", "sureness": suspect_eye_colour_sureness}
                else:
                    map["Eye color"] = {"value": suspect_eye_colour + " " + "eyes", "sureness": suspect_eye_colour_sureness}
        

 
    # 5. Suspect Facial Hair
    suspect_facial_hair = input("Does your person have a beard? (yes/no/idk): ").strip().lower()
    if suspect_facial_hair == "yes":
        suspect_facial_hair_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
        if suspect_facial_hair_sureness >= threshold:
            suspect_facial_hair_colour = str(input("What colour of facial hair does your person have?(color/ idk): ")).strip().lower()
            if suspect_facial_hair_colour == "idk":   
               map["Beard"] = {"value": "Beard", "sureness": suspect_facial_hair_sureness}
            else:
                suspect_facial_hair_colour_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
                if suspect_facial_hair_colour_sureness >= threshold:
                    suspect_facial_hair_length = str(input("How long was the beard: (short, medium, long / idk)?: ")).strip().lower()
                    if suspect_facial_hair_length == "idk":
                        map["Beard"] = {"value": suspect_facial_hair_colour + " " + "beard", "sureness": suspect_facial_hair_sureness}
                    else:
                        suspect_facial_hair_length_sureness = int(input("How sure are you on a scale from 0 to 100? "))
                        if suspect_facial_hair_length_sureness >= threshold:
                            map["Beard"] = {"value": suspect_facial_hair_length + " " + suspect_facial_hair_colour + " " + "beard", "sureness": suspect_facial_hair}    
                        else:
                            map["Beard"] = {"value": suspect_facial_hair_colour + " " + "beard", "sureness": suspect_facial_hair}    
                else:
                    map["Beard"] = {"value": suspect_facial_hair_colour + " " + "beard", "sureness": suspect_facial_hair_sureness}
   
   
   
   
   
    print("\n--- Provided Details Map ---")
    print(map)
    return map   #must return too because it is going to be passed to AI tester


