
# TubeTalk 

A Python-based web scraping project that extracts comments from a specified YouTube video and saves them to a CSV file. This scraper uses the Selenium library to automate browser actions and collect comments dynamically.

## Features

- Scrapes comments from a specified YouTube video URL.
- Allows for manual termination of the scraping process.
- Automatically stops if no new comments are detected for 1 hour.
- Limits scrolling to prevent indefinite execution.
- Saves collected comments to a CSV file.

## UseCase of this Project 

- Understand public sentiment on specific topics, brands, or content by analyzing YouTube comments.
- Can help YouTube content creators understand what their viewers are saying about their videos.
- Businesses can use the scraper to collect and analyze comments on videos about their products, services, or competitors.
- Identify trending topics and track public opinions over time based on comments.
- Use YouTube comments as a source for text data to train machine learning models, such as sentiment classifiers or language models.
-  Assess engagement levels and types of user interactions by analyzing comments across multiple videos.

## Potential Extension

- Sentiment Analysis Integration: Build sentiment analysis directly into the tool to provide instant feedback on the nature of comments.
- Keyword and Hashtag Analysis: Extract and analyze keywords and hashtags to understand trending themes.
- Scheduling and Automation: Integrate with scheduling tools to automatically run the scraper at set intervals for long-term data collection.
- Multi-Language Support: Add support for extracting and analyzing comments in multiple languages.


## Prerequisites

Before running the project, ensure you have the following installed:

- **Python 3.x**
- **Pip** (Python package installer)
- **Google Chrome** (latest version)
- **ChromeDriver** (compatible with your Chrome version (https://googlechromelabs.github.io/chrome-for-testing/#stable))

### Installation Instructions

1. **Install Python and Pip**: 
   Download and install Python from [python.org](https://www.python.org/downloads/). Pip is included with Python installations.

2. **Install Selenium**:
   Open a terminal or command prompt and run:
   ```bash
   pip install selenium
   ```

3. **Download ChromeDriver**:
   - Go to the [ChromeDriver download page](https://sites.google.com/chromium.org/driver/).
   - Download the version that matches your installed version of Chrome.
   - For Mac users on M1, ensure you download the ARM64 version if available.
   - Move the `chromedriver` executable to a directory included in your system's PATH or note its location.

4. **Clone or Download the Project**:
   Clone this repository or download it as a ZIP file and extract it.

5. **Set Up Driver Path**:
   Update the path to `chromedriver` in the script (`driver_path` variable) according to your local setup.

## How to Execute the Project

1. **Open a Terminal**:
   Navigate to the directory where you have the project files.

2. **Run the Script**:
   Execute the Python script using the following command:
   ```bash
   python3 TubeTalks.py
   ```
   

3. **Provide Video URL**:
   The script is pre-configured to scrape comments from a specific YouTube video. If you wish to change the video, modify the URL in the script accordingly.

4. **Monitor the Output**:
   - The program will start scraping comments and print progress updates in the terminal.
   - Press **ENTER** at any time to manually stop the program.

5. **Check the Output File**:
   After the program finishes execution, the comments will be saved in a CSV file located at `./Desktop/commentlist.csv` (or your specified path). You can open this file using any spreadsheet application or text editor.

## Example Usage

```bash
python3 TubeTalks.py
```

## Contributing

Contributions are welcome! If you have suggestions for improvements or features, feel free to fork the repository and submit a pull request.



