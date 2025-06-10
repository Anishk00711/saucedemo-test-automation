# SauceDemo Test Automation
This project contains end-to-end automated tests using Selenium and Pytest for [SauceDemo](https://www.saucedemo.com).

## Features Tested
- Login/logout
- Add to cart
- Cart validation
- Sorting (A-Z, Z-A, Price)
- Remove from cart

## Tech Stack
- Python
- Selenium
- Pytest

## Framework Design
- Follows Page Object Model (POM) for clean separation of concerns.
- Reusable functions for login, cart interaction, and page element verification.
- conftest.py includes fixture setup for reusable browser sessions.

## Report
- 📄 [Test Report (HTML)](./reports/report.html)
