from flask import Flask

import config
from src.controller import cloc, GitHubRepo


app = Flask(__name__)


@app.route('/')
def index():
    return "Hello, world!"


@app.route('/api', defaults={'path': ''})
@app.route('/api/<path:path>')
def api(path):
    user, repo = path.split("/")
    with GitHubRepo(user, repo) as gh:
        return cloc(gh.repo_path)
    
        

