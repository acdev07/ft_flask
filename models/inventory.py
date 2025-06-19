from bson.objectid import ObjectId
from datetime import datetime

class Inventory:
    def __init__(self, db):
        self.collection = db['inventory']

    def create_item(self, data):
        data['date'] = datetime.strptime(data['date'], "%Y-%m-%d")
        data['amount'] = data['units'] * data['cost_per_unit']
        return self.collection.insert_one(data)

    def get_all_items(self):
        return list(self.collection.find())

    def get_item_by_id(self, item_id):
        return self.collection.find_one({"_id": ObjectId(item_id)})

    def update_item(self, item_id, data):
        if 'date' in data:
            data['date'] = datetime.strptime(data['date'], "%Y-%m-%d")
        if 'units' in data and 'cost_per_unit' in data:
            data['amount'] = data['units'] * data['cost_per_unit']
        elif 'units' in data or 'cost_per_unit' in data:
            existing = self.get_item_by_id(item_id)
            if existing:
                units = data.get('units', existing['units'])
                cost = data.get('cost_per_unit', existing['cost_per_unit'])
                data['amount'] = units * cost
        return self.collection.update_one({"_id": ObjectId(item_id)}, {"$set": data})

    def delete_item(self, item_id):
        return self.collection.delete_one({"_id": ObjectId(item_id)})
