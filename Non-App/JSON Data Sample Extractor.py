import os
import json
import pyperclip

def get_json_sample(file_path):
    """Read a JSON file and extract the first two and last two objects as a sample."""
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            data = json.load(file)
            
            if isinstance(data, list):  # Ensure the data is a list of objects
                # Extract first two and last two objects
                first_two = data[:2]
                last_two = data[-2:]
                
                # Format the sample JSON structure using json.dumps for proper JSON formatting
                sample = {
                    "start_of_json": json.dumps(first_two),
                    "end_of_json": json.dumps(last_two)
                }
                
                return sample
            else:
                return None
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

def get_json_files_in_directory(directory):
    """Return a list of all .json files in the given directory."""
    return [f for f in os.listdir(directory) if f.endswith('.json')]

def main():
    # Get the current directory where the script is located
    current_directory = os.path.dirname(os.path.abspath(__file__))
    
    # Get all .json files in the current directory
    json_files = get_json_files_in_directory(current_directory)
    
    if not json_files:
        print("No .json files found in the current directory.")
        return

    # Iterate over each JSON file
    for json_file in json_files:
        file_path = os.path.join(current_directory, json_file)
        sample = get_json_sample(file_path)
        
        if sample:
            # Prepare the formatted string to copy to the clipboard
            formatted_sample = f"Here’s a sample of the .json file/object structure:\n{sample['start_of_json']}...{sample['end_of_json']}"
            
            # Copy to clipboard
            pyperclip.copy(formatted_sample)
            print(f"Sample from {json_file} copied to clipboard.")
        else:
            print(f"Unable to process {json_file} as JSON.")

if __name__ == "__main__":
    main()
