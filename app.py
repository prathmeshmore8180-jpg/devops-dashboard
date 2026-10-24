import datetime
import os
import platform
from flask import Flask, jsonify, render_template

app = Flask(__name__)

@app.route('/')
def dashboard():
    system_info = {
        "status": "Healthy & Online",
        "container_id": os.getenv("HOSTNAME", "Local-Host"),
        "os_platform": f"{platform.system()} {platform.release()}",
        "python_version": platform.python_version(),
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "environment": os.getenv("ENV_MODE", "Production")
    }
    return render_template('index.html', info=system_info)

@app.route('/health')
def health():
    return jsonify({
        "status": "up",
        "service": "devops-dashboard-api",
        "timestamp": datetime.datetime.now().isoformat()
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
