from logging import error
import subprocess


def run(api_key, path):
    if api_key == "":
        api_key = "8Mpsy8tdQBzdGedUlHmY0dUxKZgxqujp"
    if path == "":
        raise Exception("Error: El path no puede estar vacío")
    try:
        subprocess.run(['./modulos/api_shodan.sh', f'{api_key}', f'{path}'], stdout=subprocess.PIPE)
    except Exception as e:
        print("\n", e)