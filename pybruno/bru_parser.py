import re
import subprocess
import json
import pathlib

# a global variable representing the absolute path to the current file
current_path = pathlib.Path(__file__).parent.resolve()

def exec_node_script(node_script, file_path):
    result = subprocess.run(['node', node_script, file_path], capture_output=True, text=True)
    
    # Check for errors
    if result.returncode != 0:
        raise Exception(f"Error parsing BRU file: {result.stderr}")
    
    return result

def parse_env_file(
        file_path
        ):
    # Node.js scritpt that parses BRU files and converts them to JSON
    node_script = f'{current_path}/node/parseEnv.js'
    
    # Run the Node.js script with the BRU file path as an argument
    result = exec_node_script(node_script, file_path)
    
    # Parse the JSON output from the Node.js script
    env_json = json.loads(result.stdout)

    # now parse the JSON, since is contains extra information that we discard
    env_vars = {}
    for var in env_json['variables']:
        env_vars[var['name']] = var['value']
    return env_vars

def parse_bru_file(
        file_path,
        environment: dict = {}
        ):
    
    # Node.js scritpt that parses BRU files and converts them to JSON
    node_script = f'{current_path}/node/parseBru.js'
    
    # Run the Node.js script with the BRU file path as an argument
    result = exec_node_script(node_script, file_path)
    
    # Parse the JSON output from the Node.js script
    parsed_result = json.loads(result.stdout)

    # return parsed_result
    # if user specified an enviroment, read it
    if len(environment) > 0:
        return substitute_variables(parsed_result, environment)
    else:
        return parsed_result
    
def substitute_variable_in_string(txt, vars):
    return re.sub(r'\{\{(\w+)\}\}', lambda match: vars.get(match.group(1), match.group(0)), txt)
        
def substitute_variables(obj, env_vars):
    """
    Recursively substitute variables in the JSON object.
    """
    if isinstance(obj, dict):
        return {k: substitute_variables(v, env_vars) for k, v in obj.items()}
    elif isinstance(obj, list):
        return [substitute_variables(elem, env_vars) for elem in obj]
    elif isinstance(obj, str):
        # Substitute variables in strings
        return substitute_variable_in_string(obj, env_vars)
    else:
        return obj

if __name__ == '__main__':
    # Test usage
    bru_file_path = f'{current_path}/../tests/test.bru'
    bru_env_path = f'{current_path}/../tests/test_env.bru'

    # first, print without env
    parsed_data = parse_bru_file(bru_file_path)
    print(parsed_data)

    print("WITH ENVIRONMENT:")
    env = parse_env_file(bru_env_path)
    print(env)
    parsed_data = parse_bru_file(bru_file_path, env)
    print(parsed_data)