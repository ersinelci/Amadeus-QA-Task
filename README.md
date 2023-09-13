# Amadeus-QA-Task

This project is for achieving Test Automation requirements of a QA Engineer task by Amadeus.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installing Dependencies](#installing-dependencies)
- [Running API Tests](#running-api-tests)
- [Running UI Tests](#running-ui-tests)
- [Generating Allure Reports](#generating-allure-reports)
- [Project Structure](#project-structure)
- [Contributing](#contributing)
- [License](#license)

## Prerequisites

- Python 3.x
- pip package installer
- [Allure Command Line](https://docs.qameta.io/allure/#_installing_a_commandline) (for generating Allure reports)


## Getting Started

Follow these instructions to set up and run the project.

### Installing Dependencies

1. Clone the project repository to your local machine:

   ```
   git clone https://github.com/your-username/project-name.git
   ```
2. Install project dependencies from the `requirements.txt` file:

   ```
    pip install -r requirements.txt
   ```

## Running API Tests

In the scope of the Backend Test Requirement for this task, HTTP status codes (for GET, it should return 200) and json file structure is tested. The correct json format shown as below.

![json_format](https://github.com/ersinelci/Amadeus-QA-Task/assets/25690715/ad7ca634-0463-41e7-8658-b5a1a7d6bcf9)

The API test is written with pytest package. At the end of the tests a Allure report will be generated so to run this test following command should be used.

```
python -m pytest --alluredir=./allure-results api_test/
```

This command shows the test result in a terminal also add allure-results file.

## Running UI Tests

In the scope of UI Test requirements, search and list functionalities of the web page are tested. To accomplish this, Behave and Selenium are used. To run the tests, following command should be used.

```
python -m behave -f allure_behave.formatter:AllureFormatter -o allure-results ui_test/
```
This command also add the test results to the Allure report.

## Generating Allure Report


