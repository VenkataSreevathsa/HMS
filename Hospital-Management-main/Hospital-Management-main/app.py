from flask import Flask, request, jsonify, render_template_string

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

# HTML template with embedded JavaScript and CSS
html_template = """
<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Pharmacy Lookup</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            margin: 20px;
            background-color: #f4f4f4;
        }
        .container {
            max-width: 600px;
            margin: auto;
            background: #fff;
            padding: 20px;
            border-radius: 8px;
            box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
        }
        input[type="text"] {
            width: 100%;
            padding: 10px;
            margin: 10px 0;
            border: 1px solid #ddd;
            border-radius: 4px;
        }
        button {
            background: #007bff;
            color: #fff;
            border: none;
            padding: 10px 15px;
            border-radius: 4px;
            cursor: pointer;
        }
        button:hover {
            background: #0056b3;
        }
        .result {
            margin-top: 20px;
        }
        .result p {
            margin: 5px 0;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Pharmacy Lookup</h1>
        <p>Type a tablet name to find its details.</p>
        <input type="text" id="tabletInput" placeholder="Enter tablet name">
        <button onclick="searchTablet()">Search</button>
        <div class="result" id="result">
            <!-- Results will appear here -->
        </div>
    </div>

    <script>
        async function searchTablet() {
            const tabletName = document.getElementById("tabletInput").value.trim();
            const resultDiv = document.getElementById("result");

            if (!tabletName) {
                resultDiv.innerHTML = "<p>Please enter a tablet name.</p>";
                return;
            }

            try {
                const response = await fetch(`/api/tablets?name=${tabletName}`);
                if (response.ok) {
                    const data = await response.json();
                    resultDiv.innerHTML = `
                        <p><strong>Chemical Name:</strong> ${data.chemicalName}</p>
                        <p><strong>Usages:</strong> ${data.usages}</p>
                        <p><strong>Combinations:</strong> ${data.combinations}</p>
                    `;
                } else {
                    resultDiv.innerHTML = "<p>Tablet not found.</p>";
                }
            } catch (error) {
                resultDiv.innerHTML = "<p>An error occurred. Please try again later.</p>";
            }
        }
    </script>
</body>
</html>
"""

@app.route('/')
def home():
    return render_template_string(html_template)

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
