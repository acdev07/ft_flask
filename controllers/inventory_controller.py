from flask import Blueprint, request, jsonify, current_app
from services.inventory_price import InventoryService
from flasgger.utils import swag_from
import os

from utils.serializer import serialize

inventory_bp = Blueprint('inventory', __name__)
SWAGGER_PATH = os.path.join(os.path.dirname(__file__), '..', 'swagger', 'inventory.yml')

def get_service():
    db = current_app.config['MONGO_CLIENT']['flask_inventory_crud']
    return InventoryService(db)

@inventory_bp.route('/inventory', methods=['POST'])
@swag_from(SWAGGER_PATH, methods=['POST'])
def create():
    svc = get_service()
    data = request.json
    data['units'] = int(data['units'])
    data['cost_per_unit'] = float(data['cost_per_unit'])
    result = svc.create(data)
    return jsonify({'inserted_id': str(result.inserted_id)}), 201

@inventory_bp.route('/inventory', methods=['GET'])
@swag_from(SWAGGER_PATH, methods=['GET'])
def read_all():
    svc = get_service()
    items = svc.get_all()
    serialized = [serialize(i) for i in items]
    return jsonify(serialized), 200

@inventory_bp.route('/inventory/<item_id>', methods=['GET'])
def read_one(item_id):
    svc = get_service()
    item = svc.get_one(item_id)
    if not item:
        return jsonify({'error': 'Not found'}), 404
    item['_id'] = str(item['_id'])
    item['date'] = item['date'].strftime('%Y-%m-%d')
    return jsonify(item)

@inventory_bp.route('/inventory/<item_id>', methods=['PUT'])
def update(item_id):
    svc = get_service()
    data = request.json
    if 'units' in data:
        data['units'] = int(data['units'])
    if 'cost_per_unit' in data:
        data['cost_per_unit'] = float(data['cost_per_unit'])
    result = svc.update(item_id, data)
    return jsonify({'updated': result.modified_count})

@inventory_bp.route('/inventory/<item_id>', methods=['DELETE'])
def delete(item_id):
    svc = get_service()
    result = svc.delete(item_id)
    return jsonify({'deleted': result.deleted_count})

