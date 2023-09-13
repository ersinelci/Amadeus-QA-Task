# Amadeus-QA-Task

This project showcases the implementation of both API and UI tests for the Amadeus application, designed to ensure its quality and reliability.

## Table of Contents

- [Prerequisites](#prerequisites)
- [Getting Started](#getting-started)
  - [Installing Dependencies](#installing-dependencies)
- [Running API Tests](#running-api-tests)
- [Running UI Tests](#running-ui-tests)
- [Generating Allure Reports](#generating-allure-reports)
- [Project Structure](#project-structure)

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

In the scope of the Backend Test Requirement for this task, HTTP status codes (for GET, it should return 200) and JSON file structure is tested. The correct JSON format is shown below.

![json_format](https://github.com/ersinelci/Amadeus-QA-Task/assets/25690715/ad7ca634-0463-41e7-8658-b5a1a7d6bcf9)

The API test is written with pytest package. At the end of the tests an Allure report will be generated so to run this test following command should be used.

```
python -m pytest --alluredir=./allure-results api_test/
```

This command shows the test result in a terminal and also adds to allure-results file.

## Running UI Tests

In the scope of UI Test requirements, search and list functionalities of the web page are tested. To accomplish this, Behave and Selenium are used. To run the tests, the following command should be used.

```
python -m behave -f allure_behave.formatter:AllureFormatter -o allure-results ui_test/
```
This command also adds the test results to the Allure report.

## Generating Allure Reports

After running both UI Tests and API Tests, an Allure report should be generated to get insights about the tests. To generate an Allure report, the following command can be used.

```
allure serve
```

It will generate an Allure report as shown below. The report is generated as an HTML file displaying test performance and detailed information about our test results.

![allure_1](https://github.com/ersinelci/Amadeus-QA-Task/assets/25690715/2512a3c2-9209-4769-b8c5-4ab961fc55c9)

Also, test suites can be viewed one by one, so detailed information about every single test suite can be achieved.

![allure_2](https://github.com/ersinelci/Amadeus-QA-Task/assets/25690715/f3f372c2-c89e-4e57-bcf4-9f09f1d94e15)

In addition to this, there's a screenshot tab that take screenshots when a test fails.

![allure_3](https://github.com/ersinelci/Amadeus-QA-Task/assets/25690715/cb035348-25b0-4638-a75d-131853e4221b)


## Project Structure

The project is structured as an instance of Page Object Model(POM). 

> POM is a design pattern which is commonly used in Selenium for Automating the Test Cases. This design pattern can be used with any kind of framework like keyword-driven, Data-driven, hybrid framework, etc.
> The Page object is an object-oriented class which acts as an interface for the page of your Application under test. Page class contains web elements and methods to interact with web elements. While Automating the test cases, we create the object of these Page > > Classes and interact with web elements by calling the methods of these classes.
>
> source: GeeksforGeeks

So the project structure according to Page Object Model(POM) is shown as below.

```
Amadeus-QA-Task/
│
├── api_test/
│   ├── get_flights_test.py
│
├── ui_test/
│   ├── features/
│   │   ├── flights_list.feature
│   │   └── flights_search.feature
│   ├── pages/
│   │   ├── base_page.py
│   │   ├── search_page.py
│   │   └── list_page.py
│   ├── steps/
│   │   ├── common_steps.py
│   │   ├── flights_list_steps.py
│   │   └── flights_search_steps.py
│   ├── environment.py
|
├── requirements.txt
├── config.py
├── .gitignore
└── README.md
```
If you have any questions about the task, please don't hesitate the contact me via ersinelci@gmail.com
