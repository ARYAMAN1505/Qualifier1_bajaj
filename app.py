from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/bfhl', methods=['GET', 'POST'])
def bfhl():
    if request.method == 'GET':
        return jsonify({
            "operation_code": 1
        }), 200

    if request.method == 'POST':
        data = request.json.get('data', [])
        user_id = "your_full_name_ddmmyyyy"  # replace with actual format
        email = "your_email@college.edu"  # replace with your email
        roll_number = "your_roll_number"  # replace with your roll number
        
        numbers = [item for item in data if item.isdigit()]
        alphabets = [item for item in data if item.isalpha()]
        lowercase_alphabets = [char for char in alphabets if char.islower()]
        highest_lowercase_alphabet = [max(lowercase_alphabets)] if lowercase_alphabets else []
        
        return jsonify({
            "is_success": True,
            "user_id": user_id,
            "email": email,
            "roll_number": roll_number,
            "numbers": numbers,
            "alphabets": alphabets,
            "highest_lowercase_alphabet": highest_lowercase_alphabet
        }), 200

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
