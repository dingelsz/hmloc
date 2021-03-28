import sys, os
sys.path.insert(0, os.path.abspath("./app"))

from src.controller import GitHubRepo
import pathlib
import pytest

def test_gh_valid():
    with GitHubRepo("dingelsz", "emacs") as gh:
        path = gh.repo_path
        assert path
    assert not pathlib.Path(path).exists(), "issue with cleanup"

def test_gh_invalid():
    with pytest.raises(ValueError):
        with GitHubRepo("doesnt_exist", "some_repo") as gh:
            pass
