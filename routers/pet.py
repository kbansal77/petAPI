from fastapi import APIRouter, HTTPException, Request
from typing import Dict, List
from models import Pet
from firebase_admin import firestore
from routers import db

router = APIRouter()

@router.get("/")
def get_all_pets():
    try:
        pets_data = []
        pets = db.collection(u"pet_store")
        pets_ref = pets.get()

        for pet in pets_ref:
            pet_data = pets.document(pet.id).get().to_dict()
            owner_ref = db.collection(u"owner").document(pet_data["owner_id"]).get()
            if owner_ref.exists:
                owner_data = owner_ref.to_dict()
                pet_data["pets"] = owner_data["pets"]
                pet_data["owner_age"] = owner_data["owner_age"]
                pet_data["email"] = owner_data["email"]
                pet_data["owner_name"] = owner_data["owner_name"]
                pet_data["address"] = owner_data["address"]
                pet_data["contact"] = owner_data["contact"]
                pets_data.append(pet_data)
            
            else:
                raise Exception()

        return pets_data
    except Exception as e:
        print(e)
        raise HTTPException(status_code=400, detail=str(e))

@router.get("/{pet_id}")
def get_pet_info(pet_id):
    try:
        pet_ref = db.collection(u"pet_store").document(pet_id).get()
        if pet_ref.exists:
            pet_data = pet_ref.to_dict()
            owner_ref = db.collection(u"owner").document(pet_data["owner_id"]).get()
            if owner_ref.exists:
                owner_data = owner_ref.to_dict()
                pet_data["pets"] = owner_data["pets"]
                pet_data["owner_age"] = owner_data["owner_age"]
                pet_data["email"] = owner_data["email"]
                pet_data["owner_name"] = owner_data["owner_name"]
                pet_data["address"] = owner_data["address"]
                pet_data["contact"] = owner_data["contact"]
            
            else:
                raise Exception()

        else:
            raise Exception()

        return pet_data

    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, details=str(e))


@router.put("/{pet_id}")
def edit_pet(pet_id, pet: Pet):
    try:
        pet_ref = db.collection(u"pet_store").document(pet_id)
        pet_ref.update(pet.dict(exclude_none=True, exclude_defaults=True))
        

    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, details=str(e))


@router.delete("/{pet_id}")
def delete_pet(pet_id):
    try:
        pet_ref = db.collection(u"pet_store").document(pet_id)
        pet_data = pet_ref.get()
        if pet_data.exists:
            print(pet_data.to_dict()["owner_id"])
            owner_ref = db.collection(u"owner").document(pet_data.to_dict()["owner_id"])
            owner_ref.update({
                u"pets": firestore.ArrayRemove([pet_id])
            })
            pet_ref.delete()
        
        else:
            raise Exception()


    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, details=str(e))


@router.get("/{pet_id}/owner")
def get_pet_owner(pet_id):
    try:
        pet_ref = db.collection(u"pet_store").document(pet_id).get()
        if pet_ref.exists:
            pet_data = pet_ref.to_dict()
            owner_ref = db.collection(u"owner").document(pet_data["owner_id"]).get().to_dict()
            return owner_ref
        
        else:
            raise Exception()


    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, details=str(e))

@router.post("/{owner_id}")
def add_pet(owner_id, pet: Pet):
    try:
        owner = db.collection(u"owner").document(owner_id)
        owner_ref = owner.get()
        if owner_ref.exists:
            pets_ref = db.collection(u"pet_store")
            pet.owner_id = owner_id
            pet_ref = pets_ref.add(dict(pet))
            owner.update({
                u"pets": firestore.ArrayUnion([pet_ref[1].id])
            })


        else:
            raise Exception()


    except Exception as e:
        print(e)
        raise HTTPException(status_code=404, details=str(e))