import subprocess

subprocess.run(["ping", "googlle.com"])
res = subprocess.run(["nslookup", "8.8.8.8"], capture_output=True)
print(res)
print("\nThe return Code is: ", res.returncode)
print(res.stdout)
print(res.stdout.decode())
print(res.stdout.decode().split()[3:])

res2 = subprocess.run(["rm", "1567"], capture_output=True)
print(res2.returncode)
print(res2.stderr)