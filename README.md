# YTDown: Command-Line YouTube Downloader

**YTDown** is a lightweight Python-based command-line tool that allows you to effortlessly download YouTube videos and audio content. Whether you want to save your favorite videos for offline viewing or further processing, **YTDown** has you covered.

## Installation

1. Make sure you have Python installed on your system.
2. Clone the **YTDown** repository from GitHub:

    ```bash
    git clone https://github.com/your-username/YTDown.git
    ```

3. Navigate to the project directory:

    ```bash
    cd YTDown
    ```

4. Install the required dependencies (PyTube):

    ```bash
    pip install pytube
    ```

## Usage

1. Run the `main.py` script:

    ```bash
    python main.py
    ```

2. Enter a valid YouTube video URL when prompted.
3. **YTDown** will display available video streams and resolutions.
4. Select the desired resolution by entering the corresponding number.
5. The video will be downloaded to your default Downloads folder.

## Example

```bash
Enter the YouTube video URL (or type 'quit' to exit): https://www.youtube.com/watch?v=your-video-id
1. 720p (MP4)
2. 360p (MP4)
Enter the number of the resolution to download: 1
Downloading video... [####################################] 100%
Video saved as: your-video-title.mp4
```

## Note

- If no downloadable video streams are found, **YTDown** will prompt you to try another URL.
