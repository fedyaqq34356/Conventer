from pathlib import Path

def scan_files(directory):
    files = []
    
    for item in directory.iterdir():
        if item.is_file():
            files.append(item)
    
    return sorted(files)