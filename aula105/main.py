import subprocess

# ping 127.0.0.1


proc =  subprocess.run(
    ['ping', '127.0.0.1'],
    capture_output=True,
    text=True
)

# print(proc.stderr)
saida = proc.stdout
print(saida)
# print(proc.returncode)
# print(proc.args)