# YouTube Guitar Tab Parser

YouTube Guitar Tab Parser is a Python tool designed to download and parse guitar tablature from YouTube videos, and compile it into a PDF.

## Features

- Download guitar videos from YouTube
- Parse the video to extract guitar tablature
- Compile the extracted tablature into a PDF

## Requirements

- Python 3.8+
- uv

## Installation

1.  **Clone the repository**:

    ```sh
    git clone https://github.com/your-username/youtube-guitar-tab-parser.git
    cd youtube-guitar-tab-parser
    ```

2.  **Create and activate a virtual environment**:

    ```sh
    uv venv
    source .venv/bin/activate
    ```

3.  **Install the required libraries**:

    ```sh
    uv pip install -r requirements.txt
    ```

## Usage

1.  **Run the script from the command line**:

    ```sh
    python main.py "<youtube_url>" <output_directory>
    ```

    -   `<youtube_url>`: The URL of the YouTube video you want to parse.
    -   `<output_directory>`: The path to an empty directory where you want to save the generated PDF and other files.

2.  **Follow the prompts**:

    The script will prompt you to select the rectangle that contains the tablature in the image. Drag the mouse from the top-left to the bottom-right corner while holding the mouse button. The final PDF will be saved in the specified output directory.

## Example

If you run the script on [this song](https://www.youtube.com/watch?v=YiC3nvYPPas), the beginning of the output will look like this:

![image](https://github.com/user-attachments/assets/c0a3533a-45d3-4b4c-9ea4-de7378fa5738)

**Note**: For some guitarists, the end of one line may share a measure with the beginning of the next. This might be improved in a future update, but it works reasonably well for now.

## Contributing

Contributions are welcome! Please open an issue or submit a pull request for any improvements or bug fixes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.
