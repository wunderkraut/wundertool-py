
# Use argparse for basic help and usage of the tool.
import argparse

# Use PyYAML to parse settings file etc.
import yaml

# Get the submodules.
import wundertool.helpers
import wundertool.commands

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('command')
    args = parser.parse_args()
    try:
        func = getattr(wundertool.commands, args.command)
    except AttributeError:
        # TODO: Print usage instructions here.
        print("Command not found!")
    except:
        print("Unexpected error:", sys.exc_info()[0])
        raise
    else:
        func()

def settings():
    return yaml.load(open('wundertool-settings.yml'))
