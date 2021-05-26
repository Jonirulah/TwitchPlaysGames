# Load all languages
import os
import yaml

# Load config
dir_path = os.path.dirname(os.path.realpath(__file__))
with open(dir_path + "\\settings.yaml", 'r') as f:
    conf = yaml.safe_load(f)
