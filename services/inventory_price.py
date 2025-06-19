from models.inventory import Inventory

class InventoryService:
    def __init__(self, db):
        self.model = Inventory(db)

    def create(self, data):
        return self.model.create_item(data)

    def get_all(self):
        return self.model.get_all_items()

    def get_one(self, item_id):
        return self.model.get_item_by_id(item_id)

    def update(self, item_id, data):
        return self.model.update_item(item_id, data)

    def delete(self, item_id):
        return self.model.delete_item(item_id)
