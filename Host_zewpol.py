from flask import Flask, render_template, send_from_directory
import os

app = Flask(__name__, static_folder='assets', template_folder='.')

# Route to serve the main ZewpolOS interface
@app.route('/')
def index():
    return render_template('arch/index.html')

# Endpoint for your "App Store" logic
@app.route('/api/apps')
def get_apps():
    # Logic to list apps in your ZewpolOS directory
    return {"apps": ["Z-Writer", "Cube Spy", "Z-Browser"]}

if __name__ == '__main__':
    # Hosting on port 8080
    app.run(host='0.0.0.0', port=8080, debug=True)
