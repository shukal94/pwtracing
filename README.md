[![Allure Report](https://img.shields.io/badge/Allure_Report-Live-green?logo=githubpages)](https://shukal94.github.io/pwtracing/)

## Requirements
[Python 3.12+](https://www.python.org/downloads/)

[Java 8+ (version 21 recommended)](https://www.oracle.com/java/technologies/downloads/#jdk21-mac)

[Allure](https://allurereport.org/docs/install/)

## Install
1. Go to project root - `cd /path/to/pwtracing`
2. Install virtual env - `python -m venv .venv`
2. Activate virtual env - `source .venv/bin/activate` (Linux/Mac), `.\.venv\Scripts\activate` (Windows)
3. Install dependencies - `pip install -r requirements.txt`
4. Install browsers - `playwright install`

## Run
*Mac/Linux* `sh scripts/run_smoke.sh`

*Windows* `.\scripts\run_smoke.bat`

## See reports
`allure serve`
