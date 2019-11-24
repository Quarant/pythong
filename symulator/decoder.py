m={
    "01":{
        "name":"ENGINE",
        "010": "speed",
        "020": "gear indicator"
        },
    "46":{
        "name": "COMFORT",
        "010":"Windows",
        "100": "Mirrors"
        },
    "03":{
        "name":"ABS",
        "001":"ABS",
        "010":"TC"
        },

    "08":{
        "name":"HVAC",
        "001":"temp",
        "010":"zone"
        },

    "16":{
        "name":"STEERING",
        "001":"rotation",
        "010":"mode"
        },

    "37":{
        "name": "NAVIGATION",
        "001" : "Height",
        "010" : "Latitude",
        "020" : "Longitude",
        "100" : "number"
        },

    "56":{
        "name": "RADIO",
        "010" : "Band",
        "050" : "Current",
        "100" : "RDS"

        },

    "35":{
        "name": "CENTRAL LOCK",
        "001": "door lock status"
        }
    
}


def decode(msg):
    try:
        tmp=m[msg[0:2]]
        name = tmp["name"]
        function = tmp[ msg[2:5] ]
        data = msg[5:11]
        # return "CAN: {} name: {} \"{}\" function: {} \"{}\" data: {} \"{}\" ".format(msg,name,msg[0:2],function,msg[2:5],data,msg[5:])
        return {"name":name,"function":function,"data":data}
    except Exception:
        return msg
        