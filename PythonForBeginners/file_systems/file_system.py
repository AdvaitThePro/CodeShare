from pathlib import Path

# What is the current directory?
cwd = Path.cwd()
print("\nCurrent Directory is:\n" + cwd)

# Create full path name 
new_file = Path.joinpath(cwd, "new_file.txt")
print("\nFull Path\n" + str(new_file))

# Check If file exists
print('\nDoes that file exist? ' + str(new_file.exists()) + '\n')

