import datetime
import os
import platform
import uuid
from flask import Flask, jsonify, render_template, request

app = Flask(__name__)

# In-memory Agile Ticket Store with pre-loaded Sprint tasks
tickets_db = [
    {
        "id": "SCRUM-101",
        "title": "Setup Dockerfile & Multi-stage build",
        "priority": "High",
        "status": "done"
    },
    {
        "id": "SCRUM-102",
        "title": "Configure GitHub Actions CI Pipeline",
        "priority": "Medium",
        "status": "in_progress"
    },
    {
        "id": "SCRUM-103",
        "title": "Implement Sprint Velocity & Burndown tracking",
        "priority": "Low",
        "status": "todo"
    }
]

@app.route('/')
def dashboard():
    system_info = {
        "status": "Healthy & Online",
        "container_id": os.getenv("HOSTNAME", "Local-Host"),
        "os_platform": f"{platform.system()} {platform.release()}",
        "python_version": platform.python_version(),
        "timestamp": datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
        "sprint": "Sprint 1 (Active)"
    }
    return render_template('index.html', info=system_info, tickets=tickets_db)

@app.route('/api/tickets', methods=['GET', 'POST'])
def handle_tickets():
    if request.method == 'POST':
        data = request.get_json() or {}
        title = data.get("title", "").strip()
        if not title:
            return jsonify({"error": "Ticket title is required"}), 400
        
        new_ticket = {
            "id": f"SCRUM-{str(uuid.uuid4())[:4].upper()}",
            "title": title,
            "priority": data.get("priority", "Medium"),
            "status": "todo"
        }
        tickets_db.append(new_ticket)
        return jsonify(new_ticket), 201
    
    return jsonify(tickets_db), 200

@app.route('/api/tickets/<ticket_id>/move', methods=['POST'])
def move_ticket(ticket_id):
    data = request.get_json() or {}
    new_status = data.get("status")
    if new_status not in ["todo", "in_progress", "done"]:
        return jsonify({"error": "Invalid status"}), 400

    for ticket in tickets_db:
        if ticket["id"] == ticket_id:
            ticket["status"] = new_status
            return jsonify(ticket), 200

    return jsonify({"error": "Ticket not found"}), 404

@app.route('/api/tickets/<ticket_id>', methods=['DELETE'])
def delete_ticket(ticket_id):
    global tickets_db
    tickets_db = [t for t in tickets_db if t["id"] != ticket_id]
    return jsonify({"deleted": ticket_id}), 200

@app.route('/health')
def health():
    return jsonify({
        "status": "up",
        "service": "agile-devops-board",
        "timestamp": datetime.datetime.now().isoformat()
    }), 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)