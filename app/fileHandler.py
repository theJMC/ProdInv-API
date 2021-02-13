import json

baseURL = '/app'

def getItems():
    with open(f'{baseURL}/resources/itemList.json', 'r') as file:
        dump = file.readlines()
        data = json.loads(''.join(dump))
        return(data)

if __name__ == "__main__":
    getItems()