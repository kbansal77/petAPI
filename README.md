# petAPI

## Steps to use petAPI

### Install 'Requirements.txt'
```
pip install -r requirements.txt
```
### Run Server

```
uvicorn main:app --reload
```

### Open Local Server / Docs

```
http://127.0.0.1:8000/docs#/
```

## Data Structure

| Key           | Data Type     |
| ------------- |:-------------:|
| `pet_age`      | `int` |
| `breed`      | `str` |
| `pet_gender` | `bool`      |
| `pet_name` | `str`      |
| `address` | `str`      |
| `owner_age` | `int`      |
| `contact` | `str`      |
| `email` | `EmailStr`      |
| `owner_name` | `str`      |


## Call API

### /pet/

Method : Get

Description: Get All Pets


Response:
```
[
  {
    "pet_age": 24,
    "owner_id": "i68jKCQTWKKVyoFoGpQP",
    "breed": "hushky",
    "pet_name": "Rambo",
    "pet_gender": true,
    "pets": [
      "E5slfHamcFg0oTyVk1Pb"
    ],
    "owner_age": 25,
    "email": "example1@gmail.com",
    "owner_name": "owner1_name",
    "address": "address1",
    "contact": "9898656532"
  },
  {
    "breed": "pub",
    "pet_age": 21,
    "owner_id": "lo0xoZsBY80z203WCE8Q",
    "pet_gender": true,
    "pet_name": "rocky",
    "pets": [
      "VmAc5CE7CrtV1nxVNUp3"
    ],
    "owner_age": 13,
    "email": "kartikbansal2000@gmail.com",
    "owner_name": "Kartik",
    "address": "fsdfihsdif",
    "contact": "9854545452"
  }
]
```

### /pet/{pet_id}

Method: Get

Description: Get specific pet's detail

Response: 
```
{
  "breed": "hushky",
  "owner_id": "i68jKCQTWKKVyoFoGpQP",
  "pet_name": "Rambo",
  "pet_age": 24,
  "pet_gender": true,
  "pets": [
    "E5slfHamcFg0oTyVk1Pb"
  ],
  "owner_age": 25,
  "email": "example1@gmail.com",
  "owner_name": "owner1_name",
  "address": "address1",
  "contact": "9898656532"
}
```

### /pet/{pet_id}

Method: Put

Description: Edit Pet Details

Request Body: 

Note: Enter only values you what to edit. Don't change owner_id
```
{
  "pet_age": 0,
  "breed": "string",
  "pet_gender": true,
  "pet_name": "string"
}
```

Response: 
```
null
```

### /pet/{pet_id}

Method: Delete

Description: Delete Pet

Response:
```
null
```

### /pet/{owner_id}

Method: Post

Description: Add Pet


Request Body: 

Note:  Don't change owner_id
```
{
  "pet_age": 0,
  "breed": "string",
  "pet_gender": true,
  "pet_name": "string"
}
```

Response: 
```
null
```

### /owner/

Method: Get

Description: Get All Owners' Details

Response:
```
[
  {
    "owner_age": 25,
    "email": "example1@gmail.com",
    "contact": "9898656532",
    "owner_name": "owner1_name",
    "address": "address1",
    "owner_id": "i68jKCQTWKKVyoFoGpQP",
    "pets_data": [
      {
        "pet_age": 24,
        "pet_gender": true,
        "pet_name": "Rambo",
        "breed": "hushky",
        "pet_id": "E5slfHamcFg0oTyVk1Pb"
      }
    ]
  },
  {
    "owner_age": 13,
    "owner_name": "Kartik",
    "contact": "9854545452",
    "address": "fsdfihsdif",
    "email": "kartikbansal2000@gmail.com",
    "owner_id": "lo0xoZsBY80z203WCE8Q",
    "pets_data": [
      {
        "breed": "pub",
        "pet_age": 21,
        "pet_gender": true,
        "pet_name": "rocky",
        "pet_id": "VmAc5CE7CrtV1nxVNUp3"
      }
    ]
  }
]
```

### /owner/

Method: Post

Description: Add New Ownwer

Request Body: 
```
{
  "address": "string",
  "owner_age": 0,
  "contact": "string",
  "email": "user@example.com",
  "owner_name": "string",
  "pets": []
}
```

Response:
```
null
```

### /owner/{owner_id}

Method: Get

Description: Get Owner's Pets

Response:
 ```
 [
  {
    "breed": "hushky",
    "owner_id": "i68jKCQTWKKVyoFoGpQP",
    "pet_name": "Rambo",
    "pet_gender": true,
    "pet_age": 24,
    "pet_id": "E5slfHamcFg0oTyVk1Pb"
  }
]
 ```
