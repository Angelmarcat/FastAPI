from fastapi import APIRouter, Response, status
from config.db import conn
from schemas.people import peopleEntity, peoplesEntity
from models.people import People
from bson import ObjectId
from starlette.status import HTTP_204_NO_CONTENT

people = APIRouter()

@people.get('/people', response_model=list[People], tags=["Person"])
def find_all_persons():
    return peoplesEntity(conn.local.people.find())

@people.post('/people', response_model=People, tags=["Person"])
def create_person(people: People):
    new_person = dict(people)
    del new_person["id"]
    id = conn.local.people.insert_one(new_person).inserted_id
    people = conn.local.people.find_one({"_id": id})
    return peopleEntity(people)

@people.get('/people/{id}')
def find_person(id: str):
    return peopleEntity(conn.local.people.find_one({"_id": ObjectId(id)}))


@people.get('/peoples/{orderBy}')
def find_person(orderBy: int):
    return peopleEntity(conn.local.people.find({"orderBy": orderBy}))
    return "recived"


@people.delete('/people', status_code=status.HTTP_204_NO_CONTENT, tags=["Person"])
def delete_person(id: str):
    peopleEntity(conn.local.people.find_one_and_delete({"_id": ObjectId(id)}))
    return Response(status_code=HTTP_204_NO_CONTENT)

@people.delete('/peoples', status_code=status.HTTP_204_NO_CONTENT, tags=["Person"])
def delete_person(orderBy: int):
    peopleEntity(conn.local.people.find_one_and_delete({"orderBy": orderBy}))
    return Response(status_code=HTTP_204_NO_CONTENT)