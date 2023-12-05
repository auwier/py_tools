# Automatic Sound Player Script with Selenium

This Python script uses the Selenium library to automatically play a sound when a specific condition is met on a web page. In this example, the script checks for a particular text content within an element identified by XPath.

## Prerequisites

- Python installed on your system.
- Selenium library installed: `pip install selenium`
- Web browser driver (e.g., ChromeDriver) downloaded and placed in a specified path.

## Setup

1. **Clone the repository:**
   ```bash
   git clone <repository_url>
   ```

2. **Install Dependencies:**
   ```bash
   pip install selenium
   ```

3. **Configure the Script:**

   Open the script (main.py) in a text editor.
- Replace <expected_text> with the expected text content.
- Replace <your_xpath> with the XPath expression to locate the target element.
- Replace <path_to_webdriver/chromedriver> with the actual path to your ChromeDriver executable.
- Replace <your_URL> with the URL of the web page you want to monitor.

## Usage
1. Run the Script:

```bash
python script.py
```
The script will start monitoring the specified web page and play a sound when the expected text is not found within the target element.

2. Terminating the Script:
Press <kbd>Ctrl</kbd> + <kbd>C</kbd> in the terminal to stop the script manually.

## Notes
- Adjust the interval_seconds variable to set the desired time interval between checks.
- Make sure to have the correct web browser driver for Selenium (e.g., ChromeDriver) installed and configured.
- Customize the driver.execute_script line to open the desired sound or URL when the condition is met.
