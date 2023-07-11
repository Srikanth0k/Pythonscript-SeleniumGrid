FROM python:3.9

# Set the working directory inside the container
WORKDIR /app

# Copy the Python script and chromedriver to the working directory
COPY scrape_quotes.py /app/
COPY chromedriver_win32/chromedriver.exe /app/chromedriver_win32/

# Install dependencies
RUN pip install selenium click webdriver_manager

# Download and install Google Chrome
RUN apt-get update && apt-get install -y wget gnupg
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add -
RUN echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" >> /etc/apt/sources.list.d/google-chrome.list
RUN apt-get update && apt-get install -y google-chrome-stable

# Set up Chrome options
ENV CHROME_BIN=/usr/bin/google-chrome-stable
ENV CHROME_DRIVER=/app/chromedriver_win32/chromedriver

# Run the Python script
CMD ["python", "scrape_quotes.py"]
