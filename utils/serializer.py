from bson import ObjectId
from datetime import datetime


def serialize(item):
    item['_id'] = str(item['_id']) if isinstance(item['_id'], ObjectId) else item['_id']

    if isinstance(item.get('date'), datetime):
        item['date'] = item['date'].strftime('%Y-%m-%d')

    return item
