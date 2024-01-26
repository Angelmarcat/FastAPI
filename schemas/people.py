def peopleEntity(item) -> dict:
    return {
        "id": str(item["_id"]),
        "name": item["name"],
        "age": item["age"],
        "orderBy": item["orderBy"],
    }

def peoplesEntity(entity) -> list:
    return [peopleEntity(item) for item in entity]