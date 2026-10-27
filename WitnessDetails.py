def getInfo():
    print("Fill the suspect's details below:\n")

    map = {}
    threshold = 70

    # 1. Suspect Gender
    suspect_gender = input("Is your person male? (yes/no): ").strip().lower()
    if suspect_gender == "yes":
        gender_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
        if gender_sureness >= threshold:
            map["Gender"] = {"value": "a photo of a man.", "sureness": gender_sureness}
    else:
        gender_sureness = int(input("How sure are you that your person is female on a scale from 0 to 100?: "))
        if gender_sureness >= threshold:
            map["Gender"] = {"value": "a photo of a woman.", "sureness": gender_sureness}

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
                    map["Hair length"] = {"value": "a photo of a person with " + suspect_hair_length + " hair.", "sureness": hair_length_sureness}

            # 2b. Hair colour
            suspect_hair_colour = str(input("What colour is the hair? (black/brown/blonde/red/gray/idk): ")).strip().lower()
            if suspect_hair_colour != "idk":
                hair_colour_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
                if hair_colour_sureness >= threshold:
                    map["Hair color"] = {"value": "a photo of a person with " + suspect_hair_colour + " hair.", "sureness": hair_colour_sureness}

    elif suspect_hair == "no":
        hair_sureness = int(input("How sure are you that they have no hair/are bald? (0-100): "))
        if hair_sureness >= threshold:
            map["Hair length"] = {"value": "a photo of a bald person.", "sureness": hair_sureness}

    # 3. Suspect Facial Hair (type, colour and length are asked separately)
    suspect_facial_hair = input("Does your person have facial hair? (yes/no/idk): ").strip().lower()
    if suspect_facial_hair == "yes":
        suspect_facial_hair_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
        if suspect_facial_hair_sureness >= threshold:

            # 3a. Type of facial hair
            facial_hair_word = "idk"   # stays "idk" unless the witness is sure of the type
            suspect_facial_hair_type = str(input("What type of facial hair? (beard/mustache/stubble/idk): ")).strip().lower()
            if suspect_facial_hair_type != "idk":
                facial_hair_type_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
                if facial_hair_type_sureness >= threshold:
                    facial_hair_word = suspect_facial_hair_type
                    if facial_hair_word == "stubble":
                        map["Facial hair"] = {"value": "a photo of a person with stubble.", "sureness": facial_hair_type_sureness}
                    else:
                        map["Facial hair"] = {"value": "a photo of a person with a " + facial_hair_word + ".", "sureness": facial_hair_type_sureness}

            # The colour and length sentences in the AI lists need to know the type,
            # so these questions are only asked when the type is known.
            if facial_hair_word != "idk":

                # 3b. Facial hair colour
                suspect_facial_hair_colour = str(input("What colour of facial hair does your person have? (black/brown/blonde/red/gray/idk): ")).strip().lower()
                if suspect_facial_hair_colour != "idk":
                    facial_hair_colour_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
                    if facial_hair_colour_sureness >= threshold:
                        if facial_hair_word == "stubble":
                            map["Facial hair colour"] = {"value": "a photo of a person with " + suspect_facial_hair_colour + " stubble.", "sureness": facial_hair_colour_sureness}
                        else:
                            map["Facial hair colour"] = {"value": "a photo of a person with a " + suspect_facial_hair_colour + " " + facial_hair_word + ".", "sureness": facial_hair_colour_sureness}

                # 3c. Beard length (only for beards)
                if facial_hair_word == "beard":
                    suspect_beard_length = str(input("How long was the beard? (short/medium/long/idk): ")).strip().lower()
                    if suspect_beard_length != "idk":
                        beard_length_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
                        if beard_length_sureness >= threshold:
                            map["Beard length"] = {"value": "a photo of a person with a " + suspect_beard_length + " beard.", "sureness": beard_length_sureness}

    elif suspect_facial_hair == "no":
        facial_hair_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
        if facial_hair_sureness >= threshold:
            map["Facial hair"] = {"value": "a photo of a clean-shaven person.", "sureness": facial_hair_sureness}

    # 4. Skin colour of a suspect
    suspect_skin_colour = str(input("How is the skin colour of your person?: (light/dark/idk): ")).strip().lower()
    if suspect_skin_colour != "idk":
        suspect_skin_colour_sureness = int(input("How sure are you on a scale from 0 to 100?: "))
        if suspect_skin_colour_sureness >= threshold:
            map["Skin colour"] = {"value": "a photo of a person with " + suspect_skin_colour + " skin.", "sureness": suspect_skin_colour_sureness}

    print("\n--- Provided Details Map ---")
    print(map)
    return map   # must return too because it is going to be passed to AI tester
