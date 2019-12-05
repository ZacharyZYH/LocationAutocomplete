from flask import Flask, jsonify, request, abort
from init import init

app = Flask(__name__)
trie, cache, limiter, keys = init(app)


@app.errorhandler(400)
def bad_request(e):
    response = jsonify({'status': 400, 'error': 'Bad Request'})
    response.status_code = 400
    return response


@app.errorhandler(401)
def unauthorized(e):
    response = jsonify({'status': 401, 'error': 'Unauthorized'})
    response.status_code = 401
    return response


@app.errorhandler(404)
def not_found(e):
    response = jsonify({'status': 404, 'error': 'Not Found'})
    response.status_code = 404
    return response


@app.errorhandler(429)
def too_many_requests(e):
    response = jsonify({'status': 429, 'error': 'Too Many Requests', 'message': str(e.limit.limit)})
    response.status_code = 429
    return response


@app.errorhandler(500)
def internal_error(e):
    response = jsonify({'status': 500, 'error': 'Internal Error'})
    response.status_code = 500
    return response


def get_modification(modify_request):
    try:
        json = modify_request.json
        key, location = json['key'], json['location']
        if key not in keys:
            abort(401)
        return location
    except KeyError as e:
        if e.args[0] == 'key':
            abort(401)
        abort(400)


@app.route('/add/', methods=['POST'])
def add():
    location = get_modification(request)
    trie.add_location(location)
    return {}, 200


@app.route('/delete/', methods=['POST'])
def delete():
    location = get_modification(request)
    try:
        trie.delete_location(location)
    except KeyError:
        pass
    return {}, 200


@cache.cached(timeout=300, key_prefix='search')
@limiter.limit("50 per hour")
@app.route('/query/', methods=['GET'])
def search():
    if request.args.get('term'):
        try:
            locations = trie.get_location_list(request.args['term'])
        except KeyError:
            locations = []
        return jsonify({'locations': locations})
    abort(400)


if __name__ == '__main__':
    app.run()
