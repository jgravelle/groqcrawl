# GroqCrawl: Advanced Web Crawling and Scraping with Streamlit and PocketGroq

![image](https://github.com/user-attachments/assets/2bf60247-6b93-47c9-aaf4-98b57a241082)


## Table of Contents
1. [Introduction](#introduction)
2. [Features](#features)
3. [Installation](#installation)
4. [Usage](#usage)
5. [Advanced Options](#advanced-options)
6. [Output Formats](#output-formats)
7. [Examples](#examples)
8. [Troubleshooting](#troubleshooting)
9. [Contributing](#contributing)
10. [License](#license)

## Introduction

GroqCrawl is a powerful and user-friendly web crawling and scraping application built with Streamlit and powered by PocketGroq. It provides an intuitive interface for extracting content from websites, with support for single-page scraping, multi-page crawling, and site mapping.

Whether you're a data scientist, researcher, or web developer, GroqCrawl offers a seamless experience for gathering web data in various formats, including Markdown, HTML, and structured data.

## Features

- **Single URL Scraping**: Extract content from individual web pages.
- **Website Crawling**: Traverse multiple pages of a website, respecting depth and page limits.
- **Site Mapping**: Generate a list of all accessible URLs within a website.
- **Multiple Output Formats**: Choose from Markdown, HTML, and structured data representations.
- **Advanced Crawling Options**: Customize your crawl with exclude/include paths, depth limits, and more.
- **Interactive Results Display**: View scraped content directly in the Streamlit interface.
- **Download Options**: Save your results as JSON files for further processing.

## Installation

1. Ensure you have Python 3.7 or later installed on your system.

2. Clone the GroqCrawl repository:
   ```
   git clone https://github.com/yourusername/groqcrawl.git
   cd groqcrawl
   ```

3. Install the required dependencies:
   ```
   pip install -r requirements.txt
   ```

4. Set up your PocketGroq API key:
   - Create a `.env` file in the project root directory.
   - Add your API key to the file: `GROQ_API_KEY=your_api_key_here`

## Usage

To run GroqCrawl:

1. Navigate to the project directory:
   ```
   cd path/to/groqcrawl
   ```

2. Launch the Streamlit app:
   ```
   streamlit run groqcrawl.py
   ```

3. Open your web browser and go to the URL displayed in the terminal (usually `http://localhost:8501`).

4. Use the interface to select your scraping type, enter a URL, and configure options.

5. Click "Run" to start the scraping/crawling process.

## Advanced Options

- **Max Depth**: Set the maximum depth for crawling (Crawl mode only).
- **Max Pages**: Limit the total number of pages to crawl (Crawl mode only).
- **Exclude Paths**: Specify URL patterns to exclude from crawling.
- **Include Only Paths**: Limit crawling to specific URL patterns.
- **Ignore Sitemap**: Skip using the sitemap.xml for crawling.
- **Allow Backwards Links**: Enable crawling of links that point to previously visited pages.

## Output Formats

1. **Markdown**: 
   - Human-readable text format.
   - Ideal for content analysis and easy viewing.

2. **HTML**: 
   - Raw HTML content of the page.
   - Useful for detailed structure analysis or further processing.

3. **Structured Data**: 
   - JSON format containing:
     - Full text content
     - Headings (h1 to h6)
     - Links (text and href)
     - Images (src and alt attributes)
     - JSON-LD data (if available)

## Examples

### Single URL Scraping

1. Select "Single URL (/scrape)" from the radio buttons.
2. Enter a URL, e.g., `https://example.com`.
3. Choose desired output formats.
4. Click "Run".

### Website Crawling

1. Select "Crawl (/crawl)" from the radio buttons.
2. Enter the starting URL, e.g., `https://example.com`.
3. Set Max Depth and Max Pages in the Options section.
4. Choose desired output formats.
5. Click "Run".

### Site Mapping

1. Select "Map (/map)" from the radio buttons.
2. Enter the website URL, e.g., `https://example.com`.
3. Click "Run".

## Troubleshooting

- **API Key Issues**: Ensure your PocketGroq API key is correctly set in the `.env` file.
- **Connection Errors**: Check your internet connection and verify the URL is accessible.
- **Slow Performance**: For large websites, try reducing Max Depth or Max Pages.
- **Missing Content**: Some websites may block scraping. Check the site's robots.txt file and consider respecting their scraping policies.

## Contributing

We welcome contributions to GroqCrawl! Please follow these steps:

1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Make your changes and commit them with clear, descriptive messages.
4. Push your changes to your fork.
5. Submit a pull request with a detailed description of your changes.

## License

GroqCrawl is released under the MIT License. See the [LICENSE](LICENSE) file for details.

---

For more information or support, please open an issue on the [GitHub repository](https://github.com/yourusername/groqcrawl/issues).

Happy crawling!
