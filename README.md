# Amazon Price Tracker (Python)

An automated Amazon price tracking script built using Python and BeautifulSoup.
The script scrapes a product page, checks if the price drops below a target value,
and sends an email alert using SMTP.

# Features
- Web scraping with BeautifulSoup
- Price extraction and comparison
- Email alerts using SMTP
- Secure environment variable handling
- Custom HTTP headers to reduce bot detection

# Tech Stack
- Python
- Requests
- BeautifulSoup
- SMTP
- python-dotenv

# Environment Variables
This project uses a `.env` file to store sensitive information such as email
credentials. The `.env` file is excluded from version control for security.

# Note
This project is intended for educational and portfolio purposes.
Live Amazon pages may block automated requests.
