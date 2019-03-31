from subprocess import Popen, PIPE, STDOUT


cmd = 'sh transform_image.sh' 
p = Popen(cmd, stdout = PIPE, 
        stderr = STDOUT, bufsize=1, shell = True)
for line in iter(p.stdout.readline, b''):
    line = line.decode("utf-8")
    print(line)
    if "reached max number of iterations" in line:
        Popen(['python3', 'transmitter.py'])


