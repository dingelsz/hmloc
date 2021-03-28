import requests as r
from zipfile import ZipFile
import pathlib
import shutil

def api_request(url, *args, **kargs):
    """ Makes a request to the given url. If there is an issue return None"""
    try:
        return r.get(url, *args, **kargs)
    except:
        return None

def rm(path):
    """If path is a file or directory it will be removed"""
    path = pathlib.Path(path)
    if not path.exists(): return
    if path.is_file(): path.unlink()
    if path.is_dir(): shutil.rmtree(path)
    


class GitHubRepo:
    """GitHubRepo is an object that represents a repository ie all the 
    files that make up that repo"""
    
    def __init__(self, user, repo, branch=None):
        self.user = user
        self.repo = repo
        self._info = None
        
        if self.info:
            self.branch = branch or self.info['default_branch']
        else:
            raise ValueError(f"Invalid repo: github.com/{self.user}/{self.repo}")

        self.zip_path = None
        self.repo_path = None

    def __repr__(self):
        return f"GitHubRepo<{self.user}, {self.repo}, {self.branch}>"

    @property
    def info(self):
        if not self._info:
            json = api_request(f"https://api.github.com/repos/{self.user}/{self.repo}").json()
            if 'message' in json and json['message'] == "Not Found":
                self._info = None
            else:
                self._info = json
        return self._info

    def __enter__(self):
        resp = api_request(f"https://api.github.com/repos/{self.user}/{self.repo}/zipball/{self.branch}")
        if resp:
            # Save the zip file
            self.zip_path = f"{self.user}_{self.repo}_{self.branch}.zip"
            with open(self.zip_path, "wb") as f:
                f.write(resp.content)
            # Extract the zip file
            zf = ZipFile(self.zip_path)
            self.repo_path = zf.namelist()[0]
            zf.extractall()
        return self

        
    def __exit__(self, type, value, traceback):
        if self.zip_path:
            rm(self.zip_path)
            self.zip_path = None
        if self.repo_path:
            rm(self.repo_path)
            self.repo_path = None
        
        

