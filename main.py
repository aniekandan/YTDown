from pytube import YouTube
from pytube.cli import on_progress

from io_handlers import (
    get_input, 
    display_video_info,
    display_download, 
    is_youtube_watchurl, 
    is_valid_selection
)
from ytinfo import get_video_info

def main() -> None:
    abort_code = 'quit'

    while True:
        # spacing between requests for watch urls
        print(end="\n\n\n")

        # get a valid youtube watch url
        ip = get_input(
            prompt=f"Enter the YouTube video URL",
            validate_callback=is_youtube_watchurl,
            abort_code=abort_code,
            error_msg="Invalid YouTube URL. Please try again."
        )

        # check if user wants to abort the loop
        if ip.lower() in [abort_code[0], abort_code]:
            break

        # rename input
        video_url = ip

        # get the video information
        video = YouTube(video_url, on_progress_callback=on_progress)
        video_info_dict = get_video_info(video)

        # check if streams/resolutions were found
        all_streams = video_info_dict['streams']        
        if video_info_dict and all_streams:
            # display the extracted video information
            display_video_info(video_info_dict)

            cancel_code = 'cancel'

            # get one of the selected resolutions
            ip = get_input(
                prompt=f"Enter the number of the resolution to download",
                validate_callback=is_valid_selection,
                abort_code=cancel_code,
                error_msg="Invalid option selected. Please try again.",
                validate_arg=len(all_streams)
            )

            # check if user wants to abort selecting resolution
            if ip.lower() in [cancel_code[0], cancel_code]:
                continue        # resume the script main loop

            # rename input
            selection = int(ip) - 1

            # display the download information and progress
            selected_stream = all_streams[selection]
            display_download(selected_stream)

        else:
            print("No downloadable video streams found. Please try another URL.")

if __name__ == "__main__":
    main()