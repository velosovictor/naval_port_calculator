def userEntity(item) -> dict:
    return {
        "id":str(item["_id"]),
        # "name":item["name"],
        # "email":item["email"],
        # "password":item["password"]
    
        "navio_parametro_01": item["navio_parametro_01"],
        "navio_parametro_02": item["navio_parametro_02"],
        "navio_parametro_03": item["navio_parametro_03"],
        "navio_parametro_04": item["navio_parametro_04"],
        "navio_parametro_05": item["navio_parametro_05"],
        "navio_parametro_06": item["navio_parametro_06"],
        "navio_parametro_07": item["navio_parametro_07"],
        "navio_parametro_08": item["navio_parametro_08"],
        "navio_parametro_09": item["navio_parametro_09"],
        "navio_parametro_10": item["navio_parametro_10"],
        "navio_parametro_11": item["navio_parametro_11"],
        "navio_parametro_12": item["navio_parametro_12"],
        "navio_parametro_13": item["navio_parametro_13"],
        "navio_parametro_14": item["navio_parametro_14"],
        "navio_parametro_15": item["navio_parametro_15"],
        "navio_parametro_16": item["navio_parametro_16"],
        "navio_parametro_17": item["navio_parametro_17"],
        "navio_parametro_18": item["navio_parametro_18"],
        "navio_parametro_19": item["navio_parametro_19"],
        "navio_parametro_20": item["navio_parametro_20"],
        "navio_parametro_21": item["navio_parametro_21"],
        "navio_parametro_22": item["navio_parametro_22"],
        "navio_parametro_23": item["navio_parametro_23"],
        "navio_parametro_24": item["navio_parametro_24"],
        "navio_parametro_25": item["navio_parametro_25"]

    }

def usersEntity(entity) -> list:
    return [userEntity(item) for item in entity]