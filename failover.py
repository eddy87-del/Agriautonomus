PRIMARY_LINK = True

def check_link():
    global PRIMARY_LINK

    if PRIMARY_LINK:
        return "PRIMARY"

    return "LORA_BACKUP"
