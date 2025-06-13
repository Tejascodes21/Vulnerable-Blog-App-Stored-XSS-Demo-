Vulnerable Blog App (Stored XSS Demo)
**XSS Demo Blog** is a lightweight Flask-based web application designed to demonstrate how **Stored Cross-Site Scripting (XSS)** vulnerabilities work in a typical blog platform.

This project serves as a hands-on learning tool for developers, security enthusiasts, and students who wish to explore how improper handling of user input can lead to severe security risks.

> ⚠️ This application is intentionally vulnerable. It should only be used in isolated environments for educational or testing purposes.

---

📌 Project Overview

The application mimics a basic blog system featuring:

- A simple login interface
- A static blog post
- A comment section that **intentionally does not sanitize user input**

By submitting JavaScript code in the comment section, users can observe how **malicious scripts are stored and executed** when the page reloads — effectively demonstrating a real-world stored XSS attack scenario.

---

🔐 Authentication

The application includes a minimal authentication layer to simulate a real-world admin login:

- **Username:** `admin`  
- **Password:** `admin`

There is no user registration or access control logic beyond this static login.


📝 Blog Page

Once logged in, you'll see:

- A static blog post
- A list of comments
- A form to submit new comments

Try adding something like this in a comment:
<script>alert('XSS')</script>


🎯 Use Case

This demo highlights:

- The impact of stored XSS in web applications
- Why input sanitization and output escaping are critical
- How even basic web apps can be vulnerable without proper security measures

---
| **Component**           | **Technology Used**                                                                 |
| ----------------------- | ----------------------------------------------------------------------------------- |
| **Frontend**            | **HTML5**, **CSS3**, **Bootstrap 4** – For structure, layout, and responsive design |
| **Backend**             | **Python 3**, **Flask** – Lightweight WSGI framework for routing and logic          |
| **Templating Engine**   | **Jinja2** – Renders dynamic content in HTML templates                              |
| **Database**            | **SQLite** – Lightweight embedded database for storing users and comments           |
| **Authentication**      | Flask session-based login with credentials (`admin/admin`)                          |
| **Vulnerability Layer** | Intentionally left unsanitized comment section to demonstrate **Stored XSS**        |
| **Local Server**        | Flask development server (`localhost:5000`) for running the app                     |
| **Environment**         | Python `venv` (optional) – For virtual environment and dependency management        |


💻 Running the Project Locally

Follow the steps below to run the application on your local machine.


1. Clone the repository
   
git clone https://github.com/Tejascodes21/Vulnerable-Blog-App-Stored-XSS-Demo.git
cd Vulnerable-Blog-App-Stored-XSS-Demo-

2. Create a virtual environment (optional but recommended)
   
python -m venv venv
source venv/bin/activate    # Windows: venv\Scripts\activate

3. Install required dependencies
   
pip install -r requirements.txt

4. Launch the application
python app.py
Open your browser and navigate to:
http://127.0.0.1:5000

🧪 Demonstrating the Vulnerability
On the blog page, try submitting the following JavaScript snippet as a comment:

<script>alert('XSS Attack!');</script>

Refresh the page to see the script execution in action. This illustrates how unsanitized input can be exploited to inject malicious code.
