# Ex 15: REST API in Python (Flask)  -> pip install flask
from flask import Flask, request, jsonify
import subprocess
import platform

app = Flask(__name__)

def run_command(command):
    try:
        result = subprocess.run(command, capture_output=True, text=True, timeout=20)
        return result.stdout if result.stdout else result.stderr
    except subprocess.TimeoutExpired:
        return "Command timed out."
    except Exception as e:
        return str(e)

@app.route('/')
def home():
    return """
    <h2>Network Performance REST API</h2>
    <p>Use the following URLs:</p>
    <ul>
        <li>/ping?host=google.com</li>
        <li>/traceroute?host=google.com</li>
        <li>/netstat</li>
    </ul>
    """

@app.route('/ping')
def ping():
    host = request.args.get('host', 'google.com')
    if platform.system().lower() == "windows":
        command = ["ping", "-n", "4", host]
    else:
        command = ["ping", "-c", "4", host]
    return jsonify({"operation": "PING", "host": host, "result": run_command(command)})

@app.route('/traceroute')
def traceroute():
    host = request.args.get('host', 'google.com')
    if platform.system().lower() == "windows":
        command = ["tracert", host]
    else:
        command = ["traceroute", host]
    return jsonify({"operation": "TRACEROUTE", "host": host, "result": run_command(command)})

@app.route('/netstat')
def netstat():
    if platform.system().lower() == "windows":
        command = ["netstat", "-ano"]
    else:
        command = ["netstat", "-tuln"]
    return jsonify({"operation": "NETSTAT", "result": run_command(command)})

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)
