# YouTube Guitar Tab Parser

YouTube Guitar Tab Parser is a Python tool designed to download and parse guitar tablature from YouTube videos, and compile it into a PDF. This code is optimized for Python 3.8 and might not work for other versions. 

## Features

- Download guitar videos from YouTube
- Parse the video to extract guitar tablature
- Compile the extracted tablature into a PDF

## Requirements

Make sure to install the following libraries:

- OpenCV
- yt_dlp
- numpy
- PIL (Pillow)

## Installation

1. **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/youtube-guitar-tab-parser.git
    cd youtube-guitar-tab-parser
    ```

2. **Install the required libraries**:

    ```sh
    pip install opencv-python yt-dlp numpy pillow
    ```

## Configuration

1. **Set the main directory**:

    Modify the path in `main_directory.py` to point to an empty directory where you want to generate the PDF. 

    ```python
    # main_directory.py
    output_directory = "/path/to/your/output/directory"
    ```

2. **Ensure all files are in the same folder**:

    Make sure that all the files needed for the script to run are in the same folder as `main_directory.py`.

## Usage

1. **Run the script**:

    ```sh
    python main.py
    ```

2. **Follow the prompts**:

    The script will prompt you (through the terminal output) to input the URL of the YouTube video you want to download and process. Later, when prompted, select the rectangle that contains the tablature in the image (drag the mouse from the top left to the bottom right corner while pressing and holding). The final PDF will be at the location listed in the terminal. 

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

This project utilizes the following libraries:

- [OpenCV](https://opencv.org/)
- [yt_dlp](https://github.com/yt-dlp/yt-dlp)
- [numpy](https://numpy.org/)
- [Pillow (PIL)](https://python-pillow.org/)
