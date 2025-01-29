# AssessmentSubmission
Elastiq.AI Take Home Assessment - Solution submission

## 🧪 Selenium Test Automation - Table Search Demo

### 📌 Overview  
This script automates a search functionality test using **Selenium WebDriver** on the [LambdaTest Selenium Playground](https://www.lambdatest.com/selenium-playground/table-sort-search-demo).

### 🔍 Test Steps  
1. **Opens the webpage** containing a searchable table.  
2. **Searches for "New York"** in the table's search box.  
3. **Verifies exactly 5 matching rows** are displayed.  
4. **Checks that the total entries message** reflects 24 total entries.  

---

## ⚙️ Setup & Prerequisites  

### 🔹 1. Install Python  
Ensure **Python 3.7+** is installed. Check your version:  
```sh
python --version
```

### 🔹 2. Set Up a Virtual Environment (Optional)

To create an isolated environment, run:

```sh
python -m venv .venv
```

Activate the virtual environment:

- **Windows:**

```sh
.venv\Scripts\activate
```

- **macOS/Linux:**

```sh
source .venv/bin/activate
```

### 🔹 3. Install Dependencies  
Run the following command to install required packages:

```sh
pip install -r requirements.txt
```

Ensure your `requirements.txt` includes:

```txt
selenium
pytest
```

### 🔹 4. Ensure Chrome & ChromeDriver Are Installed  

- **Google Chrome** must be installed on your system.
- **ChromeDriver** is automatically managed by Selenium, but if issues occur:

  1. Check your Chrome version:
  
  Open Chrome and navigate to:

  ```sh
  chrome://settings/help
  ```

  2. Download the matching ChromeDriver:
  
  Visit [ChromeDriver Download](https://sites.google.com/a/chromium.org/chromedriver/) and download the version matching your Chrome browser.

  3. Place the driver in a known directory and update your system PATH.

---

## 🚀 Running the Test  

Navigate to your project directory:

```sh
cd path/to/your/project
```

Run the test script using pytest:

```sh
pytest testnew.py
```

This will:

- ✅ Launch Chrome  
- ✅ Perform the search test  
- ✅ Close the browser after execution

For detailed logs, run:

```sh
pytest -v
```

To see `print()` statements in real-time, use:

```sh
pytest -s
```

---

## 🐞 Troubleshooting  

- **❌ "NoSuchDriverException: Unable to obtain driver for chrome"**

  Ensure Google Chrome is installed and up to date.  
  Run the following command to upgrade Selenium:

  ```sh
  pip install --upgrade selenium
  ```

- **❌ "AssertionError: Expected 5 visible rows, but got X"**

  Verify that the webpage test data has not changed.  
  Adjust wait times in `WebDriverWait(driver, 10)` if elements are loading slowly.

---

## 📜 Notes  

- No need to manually manage ChromeDriver—Selenium handles it automatically.  
- If test failures occur, verify the webpage elements and test data are still correct.  
- Consider increasing wait times (`WebDriverWait(driver, 10)`) if elements take time to load.
---
