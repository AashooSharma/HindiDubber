# ![Hindi Dubber Logo](logo.png) Hindi Dubber

Hindi Dubber is a Python-based tool that converts English videos into Hindi dubbed versions effortlessly. You can input videos directly or via YouTube URLs, and the tool processes the video to produce a Hindi-dubbed version, ensuring a seamless workflow experience. Additionally, the project supports automation via a GitHub Actions manual workflow.

[![YouTube Tutorial](https://img.shields.io/badge/YouTube-Tutorial-red)](https://www.youtube.com/watch?v=your-video-link)
[![GitHub License](https://img.shields.io/github/license/aashooSharma/hindi-dubber)](LICENSE)
[![GitHub Budget](https://img.shields.io/badge/GitHub-Budget-blue)](https://www.buymeacoffee.com/aashoosharma)

---

## Table of Contents
- [Project Logo](#project-logo)
- [Features](#features)
- [Usage](#usage)
- [Installation & Setup](#installation--setup)
- [Deployment](#deployment)
- [Project Tool Tutorial](#project-tool-tutorial)
- [Contribution & Support](#contribution--support)
- [Contact Us](#contact-us)

---

## Project Logo
![Hindi Dubber Logo](logo.png)

The logo represents the Hindi Dubber project, symbolizing its purpose of converting English video content into Hindi audio using Python automation.

---

## Features
- **Automatic Audio Extraction**: Extracts audio from video files seamlessly.
- **Speech Recognition**: Transcribes English audio to text with high accuracy.
- **Translation to Hindi**: Converts English text into Hindi using Google's Translation API.
- **Text-to-Speech Conversion**: Translates text-to-Hindi speech using the Google Text-to-Speech (`gTTS`) API.
- **Automated GitHub Actions Workflow**: Trigger the tool via GitHub Actions to automate video dubbing.
- **YouTube URL & Direct Video Support**: Input either through YouTube URLs or directly uploaded videos.

---

## Usage
Hindi Dubber supports two primary usage scenarios:
1. **Local Execution**: Process videos directly from your local environment.
2. **GitHub Actions Workflow**: Automate the Hindi dubbing process using a manual workflow via GitHub Actions.

---

## Installation & Setup

### Prerequisites
- Python 3.8 or higher
- `ffmpeg` installed on your system
- Required Python libraries (see `requirements.txt`)

### Steps

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/aashooSharma/hindi-dubber.git
    cd hindi-dubber
    ```

2. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

3. **Set Up Environment Variables**:
   - If any API keys or credentials are required, store them in a `.env` file.

4. **Directory Structure**:
   Make sure your directories are structured as follows:
   ```
   HindiDubber/
   ├── input/
   │   └── input_video.mp4
   ├── output/
   ├── temp/
   ├── main.py
   ├── requirements.txt
   └── .env
   ```

---

## Deployment

### Local Execution
- Place your video file in the `input/` directory (`input/input_video.mp4` by default).
- Run the tool using:
    ```bash
    python main.py
    ```
- The output video will be saved in the `output/` directory.

### GitHub Actions Workflow

1. Navigate to the **Actions** tab on your GitHub repository.
2. Select **Hindi Dubber Manual Workflow**.
3. Provide the necessary input parameters (input video path, output path, and release tag).
4. Click **Run workflow**. 
   
   The workflow will:
   - Set up the environment and install dependencies.
   - Process and dub the video.
   - Save and upload the output as a release asset.

### [YouTube Project Tool Tutorial](https://www.youtube.com/watch?v=your-video-link)
To get a visual walkthrough of setting up and using Hindi Dubber, check out our comprehensive tutorial on YouTube.

---

## Contribution & Support

We welcome contributions! To contribute:
1. Fork the repository.
2. Create a new branch (`feature/your-feature`).
3. Commit your changes and push them to your fork.
4. Create a Pull Request with a detailed description of your changes.

### Support Us
If you find this tool useful, consider supporting us by:
- Starring the repository 🌟
- Buying us a coffee ☕: [![Buy Me a Coffee](https://img.shields.io/badge/Buy_Me_a_Coffee-support-yellow)](https://www.buymeacoffee.com/aashoosharma)

---

## Contact Us
If you have any questions or need further assistance, feel free to reach out:

- **Instagram**: [@aashooSharma](https://instagram.com/aashoosharma)
- **LinkedIn**: [@aashooSharma](https://linkedin.com/in/aashoosharma)
- **GitHub**: [aashooSharma](https://github.com/aashooSharma)

For business inquiries or support, email us at: `aashoosharma.tech`

---

> This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
