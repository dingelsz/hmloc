import subprocess
import json

def cloc(path):
    # Run the command
    result = subprocess.run(
        f"cloc {path} --json".split(),
        stdout=subprocess.PIPE
    )
        
    # Fromat and return the results
    output = result.stdout.decode("ascii")
    output = json.loads(output)
    del output['header']
    return json.dumps(output)
    
