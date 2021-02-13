import json

def getItems():
    with open('./resources/itemList.json', 'r') as file:
        dump = file.readlines()
        data = json.loads(''.join(dump))
        print(data)

if __name__ == "__main__":
    getItems()