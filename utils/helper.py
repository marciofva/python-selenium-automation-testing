import json
import yaml
import sys
import uuid


def config_json(json_path):
    with open(json_path) as config_file:
        return json.load(config_file)


def config_yaml(yaml_path):
    with open(yaml_path, 'r') as stream:
        return yaml.safe_load(stream)


def timeout(arg=None):
    return 10


def generate_uuid(max_value):
    return str(uuid.uuid4().hex[0:max_value])


def get_environment(arg=None):
    arguments = str(sys.argv)

    if len(sys.argv) != 2:
        raise ValueError("Please provide the environment: qa | stage")

    environment_arg = tuple([arguments])[0]
    arg_formatter = environment_arg.replace("'", "").replace("]", "").replace("[", "").replace(" ", "")

    env = list(arg_formatter.split(","))[1].upper()

    check_env = env in ["QA", "STAGE"]
    if not check_env:
        env = "QA"
    return env
