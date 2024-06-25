# nuggets.ai
## An AI Powered News Application using Cohere.ai 

## Project Overview

Nuggets is a web application aggregating and summarizing news articles from various categories. It uses the News API to fetch current news and employs the Cohere AI model to generate concise summaries. The application provides an intuitive interface for users to browse news by category or search for specific topics.

## Features

1. **Category-based News**: Fetches and displays news articles from predefined categories such as General, Business, Technology, Entertainment, Sports, Science, and Health.
2. **News Summarization**: Utilizes Cohere AI to generate concise summaries of news articles, making it easier for users to grasp the key points quickly.
3. **Search Functionality**: Allows users to search for news articles on specific topics.
4. **User-friendly Interface**: Provides an intuitive and responsive design for easy navigation and reading.

## Technologies Used

- **Python**: The main programming language.
- **Flask**: For building the web application backend.
- **HTML/CSS/JavaScript**: For the frontend user interface.
- **News API**: For fetching real-time news data.
- **Cohere AI**: For generating article summaries.
- **Bootstrap**: For responsive design and styling.

## Setup and Installation

### Prerequisites

Ensure you have the following installed:
- Python 3.7 or higher
- pip (Python package installer)

### Clone the Repository

```sh
git clone https://github.com/sowmyakuruba20/nuggets.ai_cohere.git
```
### Create a Virtual Environment
```sh
python -m venv env
source env/bin/activate  # On Windows, use `env\Scripts\activate`
```
### Install Dependencies
```sh
pip install -r requirements.txt
```

### Set Up Environment Variables
Create a .env file in the project root and add your API keys:
NEWS_API_KEY=your_news_api_key_here
COHERE_API_KEY=your_cohere_api_key_here

### Run the Application
```sh
python news_app.py
```
### Usage
1. Browse News Categories: Click on category buttons to view news from specific categories.
2. Search for News: Use the search bar to find news articles on specific topics.
3. Read Summaries: Each article is presented with a concise summary for quick reading.
4. Access Full Articles: Click "Read more" to access the full article on its original source.

### Project Structure
1. news_app.py: The main Flask application script.
2. templates/index.html: The HTML template for the web interface.
3. static/: Directory for static files (CSS, images).
4. requirements.txt: List of Python dependencies.

### Contributing
Contributions to Nuggets are welcome! Please feel free to submit a Pull Request.

## Video Demonstration
Here is a video demonstration of the application in action:

https://github.com/sowmyakuruba20/nuggets.ai_cohere/assets/131414180/ff7af6f1-0966-4fb2-b479-07c60d603177

### License
This project is licensed under the MIT License - see the LICENSE.md file for details.

### Acknowledgments
1. News API for providing access to current news articles.
2. Cohere AI for their powerful text summarization capabilities.
3. Flask and Bootstrap communities for their excellent documentation and resources.


This README provides a comprehensive overview of your Nuggets project, including its features, setup instructions, and usage guidelines. You may want to adjust some details, such as the GitHub repository URL, based on your specific project setup. Also, consider adding screenshots or a demo video link if available to showcase your application's interface and functionality.
