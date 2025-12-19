from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_DIR = BASE_DIR /"data/ping"

def read_ping_data():
    contents = []
    try:
        if not BASE_DIR.exists() or not DATA_DIR.is_dir():
            raise FileNotFoundError(f"Data directory not found: {DATA_DIR}")
        
        files = list(DATA_DIR.glob("ping_*.txt"))
        
        if not files:
            raise FileExistsError(f"No Ping Data files found in: {DATA_DIR}")
        
        for file in files:
            try:
                text = file.read_text(encoding="utf-8")
                contents.append(text)        
            except Exception as e:
                print(f"Error reading {file.name} : {e} ")
                
    except Exception as e:
        print(f"Data fetch failed: {e}") 

    return contents
            