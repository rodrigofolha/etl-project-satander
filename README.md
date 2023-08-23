# Web Scraping and AI Interaction for Discussion Enrichment

This script automates the process of interacting with a web forum, enriching discussions using AI-generated content, and avoiding duplicate content.

## Features

- Automates interaction with a web forum.
- Uses AI to generate responses for enriching discussions.
- Prevents duplicate content using hashed values.

## Requirements

- Python 3.x
- pandas
- selenium
- hashlib
- openai

## Setup

1. Install the required Python packages:

   ```
   pip install pandas selenium openai
   ```

2. Download and install the appropriate [ChromeDriver](https://sites.google.com/chromium.org/driver/) version for your system.

3. Configure your OpenAI API key by replacing `{PUT YOUR OPEN AI KEY HERE!}` with your actual API key.

4. Replace `{PUT YOUR EMAIL HERE!}` and `{PUT YOUR PASSWORD HERE!}` with your login credentials.

5. Run the script:

   ```
   python crawler_public.py
   ```

## Usage

1. The script logs in to a web forum.
2. It visits discussion threads and checks for duplicate content.
3. If the content is new, it generates an AI response and adds it to the discussion.
4. The script continues to the next discussion.

## Notes

- The script assumes specific HTML elements and their attributes on the website. Adjust these as needed if the website structure changes.
- The provided code snippet may require further modifications based on updates to libraries, APIs, or web page structures.

## Disclaimer

This script is provided as-is for educational purposes. Use it responsibly and in accordance with the terms of use of the web forum and any APIs you interact with.

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.
