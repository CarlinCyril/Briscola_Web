'''Application error handlers.'''

from flask import Blueprint, jsonify, make_response

bp = Blueprint('errors', __name__)

@bp.errorhandler(404)
def not_found(error):
    return make_response(jsonify({'error': 'Not found'}), 404)