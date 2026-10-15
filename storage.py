import json

def save_to_json(data, file):
    try:
        with open(file, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=6)
        print(f"Articles have been successfully saved to {file}")
    except OSError as e:
        print(f"Error: An error occured while saving the articles --> {e}")


