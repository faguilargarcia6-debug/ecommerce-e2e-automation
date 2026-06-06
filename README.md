# 🧪 Ecommerce E2E Automation Framework

An end-to-end test automation framework built to validate critical ecommerce workflows. I developed it using Python, Selenium WebDriver, and Pytest, following the Page Object Model (POM) pattern to keep the codebase clean, maintainable, and easy to scale.

---

## 📌 Overview
I built this project to automate smoke and functional testing across the most important ecommerce features. The framework covers the full user journey — from browsing products to completing a purchase — including:

- User authentication and login validation
- Login behavior with both valid and invalid credentials
- Product browsing and navigation
- Selecting product variants (size and color)
- Adding products to the cart
- Cart persistence and state validation
- Removing products from the cart
- Purchase total calculation
- Checkout form validation
- Payment flow with valid and invalid card data
- Defect identification, documentation, and tracking

The structure separates test data, page logic, and locators — making it straightforward to maintain and adapt to different ecommerce platforms.

---
## 🎯 Project Objectives
A few things I wanted to get right with this project:

- Build a UI automation framework from scratch, following industry standards
- Apply a scalable Page Object Model architecture
- Cover both positive and negative test scenarios
- Sharpen my debugging and failure analysis skills
- Practice defect reporting and test documentation
- Get hands-on experience automating real ecommerce workflows
---
## 🧱 Architecture
The framework follows a modular structure that separates responsibilities clearly:
```
project/
│
├── data/                         # Test data management
│   ├── checkout_data.py
│   ├── data_checkout.py
│   └── data_login.py
│
├── locators/                     # Centralized UI locators
│   ├── cart_locators.py
│   ├── checkout_locators.py
│   ├── login_locators.py
│   └── products_locators.py
│
├── pages/                        # Page Object Model implementation
│   ├── cart_pages.py
│   ├── checkout_pages.py
│   ├── login_pages.py
│   └── products_pages.py
│
├── test/                         # Automated test suites
│   ├── cart_test.py
│   ├── checkout_test.py
│   ├── login_test.py
│   └── product_test.py
│
├── config.py                     # Global configuration
├── conftest.py                   # Shared fixtures
├── pytest.ini                    # Custom pytest markers
├── README.md                     # Project documentation
└── .gitignore                    # Ignored files and folders
```
**Some design decisions worth noting:**

- Page Object Model keeps UI logic out of the tests themselves
- Centralized locators make selector updates painless
- Explicit waits reduce flakiness without hardcoded sleeps
- Pytest fixtures handle driver setup and teardown automatically
- Parameterized tests allow broader coverage with less repetition
---

## ⚙️ Technologies Used

* **Python 3**
* **Selenium WebDriver**
* **Pytest**
* **Page Object Model (POM)**
* **Git**
* **Github**
* **Pycharm**
---
## ️⚙️ Testing Techniques
- Data-Driven Testing
- Parameterized Tests
- Explicit Waits
- Page Object Model
- Positive and Negative Testing
- Form Validation Testing
- Guest Checkout Testing
- Defect Tracking and XFAIL Management
---

## 🚀 Installation & execution

### 1. Clone repository.

```bash
git clone https://github.com/tu-usuario/ecommerce-e2e-automation.git
cd ecommerce-e2e-automation
```

---

### 2. New virtual environment

```bash
python -m venv .venv
source .venv/bin/activate  # Linux / Mac
.venv\Scripts\activate     # Windows
```

---

### 3. Install requirements

```bash
pip install -r requirements.txt
```

---

### 4. Execute tests

```bash
pytest -v
```

---
## 🧪 Testing Strategy

### ✔ Positive Tests

- Valid login
- Add product to cart
- Guest checkout flow
- Shipping information form completion
- Payment form completion
- Cart update verification

### ✔ Negative Tests

- Invalid credentials
- Empty login fields
- Invalid card number
- Required shipping fields validation:
  - Last Name
  - Address
  - Postal Code
  - City
- Checkout blocking when mandatory information is missing
---
## Known Issues

### BUG-001: Cart drawer content does not refresh after adding products

Description:
The cart drawer UI does not update automatically after a product is added to the cart.

Impact:
Users cannot verify that the selected product was successfully added to the cart without refreshing the page or navigating to the cart page.

---

### BUG-002: Checkout cannot be completed with valid payment data

Description:
The application rejects payment completion even when valid card information is provided.

Impact:
The complete Happy Path checkout flow cannot be validated automatically.

Status:
Documented and excluded from pass/fail evaluation.
---
## Known Limitations

### KL-001: Shopify CAPTCHA blocks automated login

Description:
Shopify anti-bot protection may prevent automated authentication flows.

Impact:
Automated login tests may fail even when valid credentials are provided.

Workaround:
Guest checkout scenarios were used for checkout validation.
---
## 🧠 Best Practices Implemented

* Page Object Model (POM) architecture
* Separation of concerns between pages, locators, and test data
* Reusable test data management
* Pytest fixtures for test setup and teardown
* Parameterized test execution
* Explicit waits using WebDriverWait
* Dynamic locators and resilient element identification
* Dynamic URL handling
* Pytest markers (`skip`, `xfail`, `parametrize`)
* Iframe handling for payment fields
* Defect identification and documentation
* Differentiation between application defects and environment limitations
* Structured debugging and root cause analysis
* Maintainable and scalable test architecture

---

## 📈 Future Improvements

* CI/CD integration with GitHub Actions
* BDD implementation using Behave
* Allure reporting integration
* Screenshot capture on test failures
* Test execution using Docker containers
* Improved test data management
* Enhanced logging and debugging reports
* Failure evidence collection (screenshots and logs)