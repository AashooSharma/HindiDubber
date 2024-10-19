# Hindi Dubber

![Hindi Dubber Logo](logo.png)


**Hindi Dubber** is a powerful Python tool that converts English videos into Hindi-dubbed versions effortlessly. With options to input videos directly or via YouTube URLs, the tool processes and produces a Hindi-dubbed output efficiently. It supports automation via a GitHub Actions manual workflow, ensuring a seamless experience for users.

[![License](https://img.shields.io/github/license/aashooSharma/hindi-dubber)](LICENSE)  
[![Buy Me a Coffee](https://img.shields.io/badge/Buy_Me_a_Coffee-support-yellow)](https://buymeacoffee.com/aashoo8290b)  
[![GitHub Budget](https://img.shields.io/badge/GitHub-Budget-blue)](https://buymeacoffee.com/aashoo8290b)

---

## Table of Contents

- [Features](#features)
- [Usage](#usage)
- [Installation & Setup](#installation--setup)
- [Deployment](#deployment)
- [Project Tool Tutorial](#project-tool-tutorial)
- [Contribution & Support](#contribution--support)
- [Contact Us](#contact-us)

---

## 📋 Features

- 🎥 **Automatic Audio Extraction**: Extracts audio seamlessly from video files.
- 🗣️ **Speech Recognition**: Accurately transcribes English audio to text.
- 🌐 **Translation to Hindi**: Converts English text into Hindi using Google's Translation API.
- 🔊 **Text-to-Speech Conversion**: Generates Hindi speech using the Google Text-to-Speech (`gTTS`) API.
- 🤖 **Automated GitHub Actions Workflow**: Run the tool via GitHub Actions for automation.
- 📺 **YouTube URL & Direct Video Support**: Supports input through YouTube URLs or directly uploaded videos.

---

## 💡 Usage

Hindi Dubber can be used in two primary ways:
1. **Local Execution**: Directly run the tool from your local environment.
2. **GitHub Actions Workflow**: Automate the process using GitHub Actions for efficient video dubbing.

---

## 🔧 Installation & Setup

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
   - Store any API keys or credentials in a `.env` file if required.

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

## 🚀 Deployment

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

---

## [Project Tool Tutorial](https://www.youtube.com/watch?v=your-video-link)

[![Watch the Tutorial](yt.png)](https://www.youtube.com/watch?v=VIDEO_ID)  

Check out our comprehensive YouTube tutorial for a visual guide on setting up and using Hindi Dubber.

---

## 🤝 Contribution & Support

We welcome contributions! To contribute:

1. Fork the repository.
2. Create a new branch (`feature/your-feature`).
3. Commit your changes and push them to your fork.
4. Create a Pull Request with a detailed description of your changes.

### Support Us

If you find this tool useful, consider supporting us:

- ⭐ Star the repository
- ☕ [Buy us a coffee](https://buymeacoffee.com/aashoo8290b):  
   [![Buy Me a Coffee](https://img.shields.io/badge/Buy_Me_a_Coffee-support-yellow)](https://buymeacoffee.com/aashoo8290b)

---

## 📱 Contact Us

Have questions or need further assistance? Feel free to reach out:

- 📸 **Instagram**: [@aashooSharma](https://instagram.com/aashoosharma)
- 💼 **LinkedIn**: [@aashooSharma](https://linkedin.com/in/aashoosharma)
- 💻 **GitHub**: [aashooSharma](https://github.com/aashooSharma)

For business inquiries or support, email us at:  
`aashoosharma.tech`

---

> This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

---
