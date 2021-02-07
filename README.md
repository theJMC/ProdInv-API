# Product Inventory API Project
The JMC Product Inventory Project (JPIP) is my Python-Based Product Inventory System. There are two parts of it, the REST API webserver itself, and the Python Library used for interactions with it. 

### *STILL UNDER DEVELOPMENT ALL DOCS ARE PLANNING*

# Web Server:
The Webserver will have different routes for different functions. 

## Routes:
(All Routes Return JSON)
### `GET /list`:
The `/list` Route will list all of the items available.

### `GET /item/{itemID}`: 
This route will take in the {itemID}, and then output all of the details of that.

### `GET /item/{itemID}/{property}`:
This route will display a single property of the {itemID}.

### `POST /item`:
The POST to `/item` will create a new item entry, it will return the created item's {itemID}.

### `POST /item/{itemID}/{property}`:
This Route will take a value, and assign the item with {itemID} of the passed itemID, and assign the passed value to the property {property}

## Resources Schema:
The System will rely on two json files worth of data, the `itemList.json` file, and `clients.json`. 

#### `itemList.json` Schema:
```json
{
    "name": "{NAME}",
    "model": "{MODEL}",
    "location": "{LOCATION}",
    "takenOut": "{TAKEN_OUT}",
    "user": "{USER_ID}"
}
```

#### `clients.json` Schema:
```json
{
    "id": "{CLIENT_ID}",
    "name": "{CLIENT_NAME}",
    "email": "{CLIENT_EMAIL}"
}
```