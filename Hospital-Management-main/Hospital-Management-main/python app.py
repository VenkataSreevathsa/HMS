from flask import Flask, request, jsonify

app = Flask(__name__)

# Mock database
tablet_data = {
    "paracetamol": {
        "chemicalName": "Acetaminophen",
        "usages": "Pain relief, fever reduction",
        "combinations": "With caffeine, with codeine"
    },
    "ibuprofen": {
        "chemicalName": "Ibuprofen",
        "usages": "Anti-inflammatory, pain relief",
        "combinations": "With paracetamol, with caffeine"
    }
}

@app.route('/api/tablets', methods=['GET'])
def get_tablet_info():
    tablet_name = request.args.get('name', '').lower()
    tablet = tablet_data.get(tablet_name)
    if tablet:
        return jsonify(tablet)
    else:
        return jsonify({"error": "Tablet not found"}), 404

if __name__ == '__main__':
    app.run(debug=True)
