import glob, os, shutil
from pathlib import Path

dest_dir = Path(r"C:/Users\brind\Documents\PDFs")
source_dir = Path(r"C:\Users\brind\Documents\Voicedream Library")
for root, dirs, files in os.walk(source_dir):
    for file in files:
        if file.endswith(".pdf"):
            source = os.path.join(root, file)
            shutil.copy2(source, dest_dir)