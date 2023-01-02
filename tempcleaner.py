import os
import shutil
import getpass

username = getpass.getuser()

temp_dir = f"C:\\Users\\{username}\\AppData\\Local\\Temp"

files = os.listdir(temp_dir)

for file in files:
  filepath = os.path.join(temp_dir, file)
  try:
    if os.path.isfile(filepath):
      os.unlink(filepath)
    elif os.path.isdir(filepath):
      shutil.rmtree(filepath)
  except Exception as e:
    print(e)

print("Temporary files cleaned")


#The other files are not removed because those are being used.
#But as you can see, other files and directories are removed.