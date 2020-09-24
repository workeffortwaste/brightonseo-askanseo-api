from flask import jsonify

def api(request):
    # Handle preflight CORS headers
    if request.method == 'OPTIONS':
        # Allows GET and POST requests from any origin with the Content-Type header
        headers = {
            'Access-Control-Allow-Origin': '*',
            'Access-Control-Allow-Methods': 'GET, POST',
            'Access-Control-Allow-Headers': 'Content-Type'
        }
        return '', 204, headers

    # Set CORS headers for the main request
    headers = {
        'Access-Control-Allow-Origin': '*'
    }

    # Fetch our POST and GET data.
    request_json = request.get_json()
    print(request_json)
    request_args = request.args

    # First check to see if valid data was sent via POST
    if request_json and 'question' in request_json:
        q = request_json['question']
        return jsonify(question=q, answer='it depends'), headers
    # Else check to see if valid data was sent via GET
    elif request_args and 'question' in request_args:
        q = request_args['question']
        return jsonify(question=q, answer='it depends'), headers
    # Otherwise reply with a 400 error
    else:
        return jsonify(error='bad request'), 400, headers
