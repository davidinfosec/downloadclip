# DownloadClip Python Script

This Python script allows you to download and trim YouTube videos.

Transparency: Most of this app was created with AI assistance, as I seek to find solutions to my problems in creative ways. After finding use of such a tool, it is only fair to share it with others who may benefit in the same way.

## How to Use

1. Install the required libraries by running:

```bash
pip install pytube
```

2. Run the script and follow the prompts.

## Functions

### `download_video(url, save_path)`

Downloads a YouTube video from the provided URL and saves it to the specified directory.

### `time_to_seconds(time_str)`

Converts a time string in the format `hh:mm:ss` to seconds.

### `clip_video(input_path, output_path, start_time, end_time)`

Clips a video from the specified start time to the end time.

## Usage

1. Run the script.
2. Enter the YouTube video URL.
3. Enter the directory to save the video.
4. The video will be downloaded if it doesn't already exist in the specified directory.
5. Enter the start time (hh:mm:ss).
6. Enter the end time (hh:mm:ss).
7. The trimmed video will be saved in the same directory as `trimmed_video.mp4`.

Note: Sometimes the video lags for the first few seconds of a given clip. Acccount for this with the script by off-setting your range you want to clip by a few seconds.

## Example


https://github.com/davidinfosec/downloadclip/assets/87215831/cf50cb7b-f701-4ddf-8007-91c98499fb71

## Requirements

- Python 3.x
- `pytube` library

## License

This project is licensed under the [MIT License](LICENSE).
