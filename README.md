# Shopping Recommendation System

This is a Python-based console application that allows users to browse and choose electronics products (TVs and Mobiles), see specifications, and get redirected to Amazon or Flipkart for purchase.

It features:

* **Admin panel:** Add or delete products dynamically.
* **Customer panel:** Browse products and get real-time Email OTP verification before purchase links.
* **Text-to-Speech feedback** using `pyttsx3`.
* OTP emails are sent securely via Gmail using an App Password.

---

## Features

* Add/Delete products as an admin.
* List available TVs and Mobiles with specifications.
* OTP verification via Gmail before redirecting to purchase links.
* Web browser redirection to Amazon or Flipkart.
* Text-to-Speech greetings for a better user experience.

---

## Prerequisites

* Python 3.10+
* Pip installed

---

## Required Python Packages

Listed in `requirements.txt`:

```
pyttsx3==2.90
```

Install with:

```bash
pip install -r requirements.txt
```

---

## Gmail OTP Setup

To send OTPs securely, your Gmail account must have **2-Factor Authentication (2FA)** enabled. Follow these steps:

1. Go to your Google Account → Security.
2. Turn on **2-Step Verification**.
3. Once 2FA is enabled, go to **App Passwords**.
4. Generate a password for **Mail App**.
5. Copy the generated password.
6. Replace the placeholders in the code:

```python
EMAIL_ADDRESS = "your_email@gmail.com"
EMAIL_APP_PASSWORD = "your_generated_app_password"
```

**Note:** Do **NOT** share your email or app password publicly.

---

## How to Run

1. Clone the repository:

```bash
git clone https://github.com/Sumayya-Samreen/Shopping-Recommendation-System.git
cd Shopping-Recommendation-System
```

2. Install dependencies:

```bash
pip install -r requirements.txt
```

3. Open `shopping_recommendation_system.py` and replace email placeholders with your Gmail and app password.

4. Run the program:

```bash
python shopping_recommendation_system.py
```

5. Follow on-screen instructions:

* **Admin:** Add/delete products.
* **Customer:** Browse products and verify email OTP before being redirected to Amazon/Flipkart.

---

## Security & Privacy Notes

* Never push your real Gmail password to GitHub. Always use App Passwords.
* OTP emails will be sent only to the email entered by the customer.
* Your credentials should be kept private; do not hardcode them in public repos for production.

---

## Pro Tip for Recruiters / Collaborators

This project demonstrates a complete end-to-end workflow for a Python-based console shopping recommendation system. It highlights practical skills in:

* Designing dynamic data structures for storing products and specifications.
* Building interactive console applications with clear user navigation.
* Implementing secure OTP-based email verification using Gmail and App Passwords.
* Integrating Text-to-Speech (`pyttsx3`) for improved user experience.
* Redirecting users to web-based e-commerce platforms programmatically.
* Applying practical software engineering principles like modular code, input validation, and error handling.

It provides a clear, interpretable example of applied **Python programming, practical problem-solving, and secure user interaction implementation.**

## Author
**Sumayya Samreen — M.Sc. in Artificial Intelligence**<br>
Focused on developing practical Python-based e-commerce solutions with customer and admin modules, secure email OTP authentication, and interactive product recommendation features.
