# AssessmentSubmission
Elastiq.AI Take Home Assessment - Solution Submission

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

For setup and prerequisite instructions, please refer to the [SETUP.md](SETUP.md) file.

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

### ❌ "NoSuchDriverException: Unable to obtain driver for chrome"
- Ensure Google Chrome is installed and up to date.
- Run the following command to upgrade Selenium:
  ```sh
  pip install --upgrade selenium
  ```

### ❌ "AssertionError: Expected 5 visible rows, but got X"
- Verify that the webpage test data has not changed.
- Adjust wait times in `WebDriverWait(driver, 10)` if elements are loading slowly.

---

## 📜 Notes
- No need to manually manage ChromeDriver—Selenium handles it automatically.
- If test failures occur, verify the webpage elements and test data are still correct.
- Consider increasing wait times (WebDriverWait(driver, 10)) if elements take time to load.

---
