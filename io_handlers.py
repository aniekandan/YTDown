import re
import os

# Get the path to the Downloads folder
output_path = os.path.join(os.environ['USERPROFILE'], 'Downloads')

def get_input(prompt, validate_callback, abort_code, validate_arg=None, error_msg="Invalid Input") -> str:
    # what happens when validate_callback is the default (returns True)
    # and abort codes is an empty list?

    abort_str = f"{abort_code[0]}[{abort_code[1:]}]"
    mod_prompt = f"{prompt}, (or type '{abort_str}' to exit): "
    while True:
        ip = input(mod_prompt)
        is_valid = validate_callback(ip, validate_arg) or (ip.lower() in [abort_code[0], abort_code])

        if not is_valid:            
            print(error_msg)
            continue
        
        return ip

def is_youtube_watchurl(ip, params=None) -> bool:
    pattern = r'(https?://)?(www\.)?(youtube\.com|youtu\.be)/watch\?v=[\w-]{11}'
    if not re.match(pattern, ip):
        return False
    
    return True

def is_valid_selection(ip, max_selection) -> bool:
    try:
        selection = int(ip)

        if 1 <= selection <= max_selection:
            return True
        
        else:
            return False

    except ValueError:
        return False

def get_filesize_str(filesize: int) -> str:
    # Define the filesize units
    units = ["bytes", "KB", "MB", "GB"]
    size = filesize
    unit_index = 0

    # Loop to find the appropriate unit
    while size >= 1024 and unit_index < len(units) - 1:
        size /= 1024.0
        unit_index += 1

    # Return the formatted filesize string
    return f"{size:.2f} {units[unit_index]}"

def display_video_info(video_info):
    print(f"{video_info['title']} ({video_info['duration']})")
    for i, stream in enumerate(video_info['streams']):
        print(f"{i + 1}: {stream.resolution} - {get_filesize_str(stream.filesize)}")

def display_download(stream):
    print(f"Dowloading '{stream.title}' ({stream.resolution}) to Downloads folder.")
    stream.download(output_path=output_path)
    print("Download completed!")