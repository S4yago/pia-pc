import subprocess

def run(arg1, arg2, arg3):
  data = subprocess.run(['./api.sh', f'{arg1}', f'{arg2}', f'{arg3}'], stdout=subprocess.PIPE).stdout.decode('utf-8')
  file = open("data_github.txt", "w")
  file.write(data)
  file.close()