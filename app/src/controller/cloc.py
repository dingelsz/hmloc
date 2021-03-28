import subprocess
import json

def _format_yaml(output):
    return "<br>".join(output.splitlines()[15:]).replace(" ", "&nbsp;")

def _format_json(output):
    # Fromat and return the results
    output = json.loads(output)
    del output['header']
    return json.dumps(output)
    
def cloc(path, format="json"):
    # Run the command
    result = subprocess.run(
        f"cloc {path} --{format}".split(),
        stdout=subprocess.PIPE
    )
    output = result.stdout.decode("ascii")
    if format == 'json':
        return _format_json(output)
    if format == 'yaml':
        return _format_yaml(output)

    
    

