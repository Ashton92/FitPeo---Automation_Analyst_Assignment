# FitPeo---Automation_Analyst_Assignment

This repository provides a Python script for automating the testing of the revenue calculator on the FitPeo website using Selenium WebDriver.

Prerequisites
Software Requirements:
Python: Install Python 3.6 or later. Download it from the official Python website.
Google Chrome: Ensure Google Chrome is installed on your system.
Chrome WebDriver: Download the version compatible with your Chrome browser from ChromeDriver.
Python Libraries:
Install Selenium for Python using the following command:

bash
Copy code
pip install selenium
Installation and Setup
Clone the Repository:
Clone this repository or download the script file FitPeoTestPage.py into your local system.

Save the Script:
Save the script as FitPeoTestPage.py or use the existing filename.

Update WebDriver Path:
Update the driver_path variable in the script with the path to your Chrome WebDriver if not already in your PATH.

How to Run the Script
Open Terminal or Command Prompt:
Navigate to the directory containing the script.

Run the Script:
Execute the following command:

bash
Copy code
python FitPeoTestPage.py
Optional:
You can also open and run the script using an IDE like PyCharm or VSCode.

Features and Workflow
The script automates the following tasks:

Initialization:

Sets up the Chrome WebDriver and WebDriverWait for explicit waits.
Open Homepage:

Opens the FitPeo website and adjusts the browser window size and position.
Navigate to Revenue Calculator:

Clicks the "Revenue Calculator" link to load the calculator page.
Adjust Window Dimensions:

Dynamically resizes the browser window as needed.
Scroll to Slider:

Scrolls to the slider section of the page.
Set Slider Value:

Moves the slider to the specified value by calculating the pixel offset.
Input Number:

Clears existing values and inputs a number into the specified field.
Click Checkboxes:

Selects checkboxes corresponding to specified CPT codes and values.
Validate Total Reimbursement:

Fetches and validates the total recurring reimbursement displayed on the page.
Close Browser:

Closes the browser upon completion.
Code Snippet
Refer to the script in FitPeoTestPage.py for the detailed implementation. Here's a quick view of the main test flow:

python
Copy code
if __name__ == '__main__':
    test = FitPeoTestPage()

    test.open_homepage("https://www.fitpeo.com/")
    test.navigate_to_revenue_calculator()
    test.adjust_window(412, 915)
    test.scroll_to_slider()
    test.set_slider_value(820)
    test.adjust_window(1552, 832)
    test.input_number(560)
    test.click_checkbox('CPT-99091', '57')
    test.click_checkbox('CPT-99453', '19.19')
    test.click_checkbox('CPT-99454', '63')
    test.click_checkbox('CPT-99474', '15')
    test.validate_total_reimbursement()
    test.close_browser()
Notes
Delays in Execution:

time.sleep(2) is used after actions for better visibility of each step during execution. To optimize runtime, you can comment out or remove these delays.

Validation:
Ensure XPaths and element locators are up-to-date to match changes in the FitPeo website structure.

Browser Compatibility:
Test with the latest version of Google Chrome for compatibility.
Troubleshooting
WebDriver Errors: Verify that the Chrome WebDriver version matches your Chrome browser version.
Element Not Found: Check if the target web page structure has changed, and update XPaths accordingly.
Dependency Issues: Ensure all required Python libraries are installed.
Software and Versions
Python: Version 3.11.9
Google Chrome: Version 116 or later
Selenium: Version 4.0 or later
Conclusion
This script provides a streamlined approach to automating the FitPeo revenue calculator testing process. You can modify the script as needed for other scenarios or to accommodate changes in the website's structure.
