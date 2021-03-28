from flask import Flask, render_template, current_app, send_from_directory

import config
from src.controller import cloc, GitHubRepo


app = Flask(__name__, static_folder='src/view')


@app.route('/')
def index():
    print(app.static_folder)
    return send_from_directory(app.static_folder, "index.html")


@app.route('/api', defaults={'path': ''})
@app.route('/api/<path:path>')
def api(path):
    user, repo = path.split("/")
    with GitHubRepo(user, repo) as gh:
        return cloc(gh.repo_path)
    
        

