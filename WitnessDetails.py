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

    # 2. Suspect Hair (length and colour are asked separately)
    suspect_hair = input("Does your person have hair? (yes/no/idk): ").strip().lower()
    if suspect_hair == "yes":
        suspect_hair_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
        if suspect_hair_sureness >= threshold:

            # 2a. Hair length
            suspect_hair_length = str(input("How long is the hair? (short/medium/long/idk): ")).strip().lower()
            if suspect_hair_length != "idk":
                hair_length_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
                if hair_length_sureness >= threshold:
                    map["Hair length"] = {"value": suspect_hair_length + " hair", "sureness": hair_length_sureness}

            # 2b. Hair colour
            suspect_hair_colour = str(input("What colour is the hair? (black/brown/blonde/red/gray/idk): ")).strip().lower()
            if suspect_hair_colour != "idk":
                hair_colour_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
                if hair_colour_sureness >= threshold:
                    map["Hair color"] = {"value": suspect_hair_colour + " hair", "sureness": hair_colour_sureness}

    elif suspect_hair == "no":
        hair_sureness = int(input("How sure are you that they have no hair/are bald? (0-100): "))
        if hair_sureness >= threshold:
            map["Hair length"] = {"value": "bald", "sureness": hair_sureness}

    # 3. Suspect Facial Hair (type, colour and length are asked separately)
    suspect_facial_hair = input("Does your person have facial hair? (yes/no/idk): ").strip().lower()
    if suspect_facial_hair == "yes":
        suspect_facial_hair_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
        if suspect_facial_hair_sureness >= threshold:

            # 3a. Type of facial hair
            facial_hair_word = "facial hair"   # used in the labels if the type is unknown
            suspect_facial_hair_type = str(input("What type of facial hair? (beard/mustache/stubble/idk): ")).strip().lower()
            if suspect_facial_hair_type != "idk":
                facial_hair_type_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
                if facial_hair_type_sureness >= threshold:
                    facial_hair_word = suspect_facial_hair_type
                    map["Facial hair"] = {"value": suspect_facial_hair_type, "sureness": facial_hair_type_sureness}

            # 3b. Facial hair colour
            suspect_facial_hair_colour = str(input("What colour of facial hair does your person have? (black/brown/blonde/red/gray/idk): ")).strip().lower()
            if suspect_facial_hair_colour != "idk":
                facial_hair_colour_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
                if facial_hair_colour_sureness >= threshold:
                    map["Facial hair colour"] = {"value": suspect_facial_hair_colour + " " + facial_hair_word, "sureness": facial_hair_colour_sureness}

            # 3c. Beard length (only for beards)
            if facial_hair_word == "beard":
                suspect_beard_length = str(input("How long was the beard? (short/medium/long/idk): ")).strip().lower()
                if suspect_beard_length != "idk":
                    beard_length_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
                    if beard_length_sureness >= threshold:
                        map["Beard length"] = {"value": suspect_beard_length + " beard", "sureness": beard_length_sureness}

    elif suspect_facial_hair == "no":
        facial_hair_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
        if facial_hair_sureness >= threshold:
            map["Facial hair"] = {"value": "clean shave", "sureness": facial_hair_sureness}

    # 4. Skin colour of a suspect
    suspect_skin_colour = str(input("How is the skin colour of your person?: (light/dark/idk): ")).strip().lower()
    if suspect_skin_colour != "idk":
        suspect_skin_colour_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
        if suspect_skin_colour_sureness >= threshold:
            map["Skin colour"] = {"value": suspect_skin_colour + " " + "skin", "sureness": suspect_skin_colour_sureness}

    print("\n--- Provided Details Map ---")
    print(map)
    return map   # must return too because it is going to be passed to AI tester
