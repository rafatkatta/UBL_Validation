import uuid

from flask import Blueprint, jsonify, request, abort

admin_interface_bp = Blueprint('admin_interface', __name__)

# Datenstruktur für API-Keys und E-Mails der Benutzer
users = [
   {'username': 'user1' , 'email': 'user1@example.com' ,'api_key': 'key1', 'api_passkey': 'passkey1'},
   {'username': 'user2' , 'email': 'user2@example.com' ,'api_key': 'key2', 'api_passkey': 'passkey2'}
]

NONE_EXIST_USER= 'Benutzer existiert nicht.'

@admin_interface_bp.route('/admin/create/user', methods=['POST'])
def create_user():
    data = request.json
    username = data.get('username')
    email = data.get('email')

    if not username or not email:
        return jsonify({'message': 'Bitte gib Benutzername und E-Mail an.'}), 400

    # Annahme: Generiere API-Schlüssel und API-Passkey für neuen Benutzer
    api_key = str(uuid.uuid4())
    api_passkey =str(uuid.uuid4())

    # Speichere API-Schlüssel und API-Passkey für den neuen Benutzer
    new_user= {'username': username ,'email': email ,'api_key': api_key, 'api_passkey': api_passkey}
    users.append(new_user)

    return jsonify({
        'message': 'Benutzer erfolgreich erstellt',
        'api_key': api_key,
        'api_passkey': api_passkey,
        'email': email
    }), 201

# GET Request für Benutzerinformationen basierend auf Username oder User_email
@admin_interface_bp.route('/api/user', methods=['GET'])
def get_user():
    username = request.args.get('username')
    user_email = request.args.get('user_email')

    if not username and not user_email:
        abort(400, 'Bitte gib einen Benutzernamen oder eine Benutzer-E-Mail an.')

    for user_data in users:
        if (username and user_data['username'] == username) or (user_email and user_data['email'] == user_email):
            return jsonify({'message': 'Benutzer existiert.', 'user_data': user_data}), 200

    abort(404, NONE_EXIST_USER)

# PUT Request für Benutzeraktualisierung basierend auf Username oder User_email
@admin_interface_bp.route('/api/user/update', methods=['PUT'])
def update_user():
    username = request.args.get('username')
    user_email = request.args.get('user_email')
    new_username = request.json.get('new_username')
    new_email = request.json.get('new_email')

    if not (username or user_email) or not (new_username or new_email):
        abort(400, 'Bitte gib einen Benutzernamen oder eine Benutzer-E-Mail zum Aktualisieren an.')

    for user_data in users:
        if (username and user_data['username'] == username) or (user_email and user_data['email'] == user_email):
            # Aktualisiere Benutzerdaten
            if new_username:
                user_data['username'] = new_username
            if new_email:
                user_data['email'] = new_email

            return jsonify({'message': 'Benutzer erfolgreich aktualisiert.', 'user_data': user_data}), 200

    abort(404, NONE_EXIST_USER)

# DELETE Request für Benutzerlöschung basierend auf Username oder User_email
@admin_interface_bp.route('/api/user/delete', methods=['DELETE'])
def delete_user():
    username = request.args.get('username')
    user_email = request.args.get('user_email')

    if not username and not user_email:
        abort(400, 'Bitte gib einen Benutzernamen oder eine Benutzer-E-Mail zum Löschen an.')

    for user_data in users:
        if (username and user_data['username'] == username) or (user_email and user_data['email'] == user_email):
            # Lösche Benutzer
            users.remove(user_data)
            return jsonify({'message': 'Benutzer erfolgreich gelöscht.', 'user_data': user_data}), 200

    abort(404, NONE_EXIST_USER)

if __name__ == "__main__":
    admin_interface_bp.run(debug=True)