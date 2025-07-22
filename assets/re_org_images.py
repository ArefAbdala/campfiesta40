import os

directory = "C:\Users\arefa\Documents\GitHub\campfiesta40\images\CF2023"  # <-- Change this to your folder
files = sorted(os.listdir(directory))  # Sort alphabetically; remove 'sorted' to preserve current order

for index, filename in enumerate(files, start=1):
    old_path = os.path.join(directory, filename)
    if os.path.isfile(old_path):
        ext = os.path.splitext(filename)[1]  # Get file extension
        new_name = f"{index:02d}{ext}"       # Format as 01, 02, etc.
        new_path = os.path.join(directory, new_name)
        os.rename(old_path, new_path)