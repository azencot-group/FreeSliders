import os
import json

def generate_audio_manifest():
    audio_base = 'website_outputs/audio'
    manifest = {}
    
    if not os.path.exists(audio_base):
        print(f"Audio directory {audio_base} not found")
        return
    
    print(f"Scanning directory: {audio_base}")
    
    # Use os.listdir() to discover folders dynamically
    for folder_name in os.listdir(audio_base):
        folder_path = os.path.join(audio_base, folder_name)
        
        if os.path.isdir(folder_path):
            print(f"Processing folder: {folder_name}")
            
            folder_info = {
                'name': folder_name,
                'files': [],
                'has_prompts': False,
                'prompts': {
                    'negative': 'Low intensity',
                    'neutral': 'Neutral',
                    'positive': 'High intensity'
                }
            }
            
            # Check for p.json
            p_json_path = os.path.join(folder_path, 'p.json')
            if os.path.exists(p_json_path):
                try:
                    with open(p_json_path, 'r') as f:
                        folder_info['prompts'] = json.load(f)
                        folder_info['has_prompts'] = True
                        print(f"  ✓ Loaded prompts from p.json")
                except Exception as e:
                    print(f"  ✗ Error loading p.json: {e}")
            
            # Get all audio files using os.listdir()
            for file_name in os.listdir(folder_path):
                if file_name.lower().endswith(('.mp3', '.wav', '.ogg', '.m4a')):
                    folder_info['files'].append(file_name)
                    print(f"  ✓ Found audio file: {file_name}")
            
            # Sort files by scale if possible
            folder_info['files'].sort(key=lambda x: extract_scale(x) if extract_scale(x) is not None else x)
            
            if folder_info['files']:
                manifest[folder_name] = folder_info
                print(f"  Added {len(folder_info['files'])} files to manifest")
    
    # Save manifest to the website folder
    manifest_path = 'website_outputs/audio_manifest.json'
    with open(manifest_path, 'w') as f:
        json.dump(manifest, f, indent=2)
    
    print(f"\n✓ Generated manifest at {manifest_path}")
    print(f"✓ Found {len(manifest)} folders with audio files:")
    for folder, info in manifest.items():
        print(f"  - {folder}: {len(info['files'])} files")

def extract_scale(filename):
    import re
    match = re.search(r'scale_(-?\d+\.?\d*)', filename)
    return float(match.group(1)) if match else None

if __name__ == "__main__":
    generate_audio_manifest()