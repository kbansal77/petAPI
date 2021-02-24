from fastapi import APIRouter, HTTPException, Request
from typing import Dict, List
from models import Pet, Owner
from firebase_admin import firestore
from routers import db

router = APIRouter()


@router.get("/")
def get_owners():
    try:
        owners_data = []
        owners = db.collection(u"owner")
        owners_ref = owners.get()
        for owner in owners_ref:
            owner_data = owners.document(owner.id).get().to_dict()
            owner_data["owner_id"] = owner.id
            owner_data["pets_data"] = []
            for pet in owner_data["pets"]:
                print(pet)
                pet_ref = db.collection(u"pet_store").document(pet).get().to_dict()
                pet_ref["pet_id"] = pet
                pet_ref.pop("owner_id")
                owner_data["pets_data"].append(pet_ref)
            owner_data.pop("pets")
            owners_data.append(owner_data)
        return owners_data
        

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


@router.get("/{owner_id}")
def get_owner_pet(owner_id):
    try:
        owner_pets = []
        owner_ref = db.collection(u"owner").document(owner_id).get()
        if owner_ref.exists:
            owner_data = owner_ref.to_dict()
            for pet in owner_data["pets"]:
                pet_ref = db.collection(u"pet_store").document(pet).get().to_dict()
                pet_ref["pet_id"] = pet
                owner_pets.append(pet_ref)
            return owner_pets
        
        else:
            raise Exception()

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))


@router.post("/")
def add_owner(owner: Owner):
    try:
        owner_ref = db.collection(u"owner")
        owner_add = owner_ref.add(dict(owner))

    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))