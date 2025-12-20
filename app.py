from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def home():

    skills = [
        "Python Programming (Scripting, Automation, Data Analysis)",
        "Data Analytics & Automation (Pandas, NumPy, Excel, Selenium)",
        "IT Operations & Utility Systems (AMISP, HES, MDMS)",
        "Electrical & Control Systems (Power Systems, Machines, MATLAB)",
        "Web Development (Flask, HTML, CSS, JavaScript)",
        "Project Reporting, Vendor Coordination, and Operations Support",
        "Languages: English, Hindi"
    ]

    projects = [
        {
            "title": "Consumer Data Web Application",
            "description": (
                "Developed a Flask-based web application with MongoDB to manage "
                "consumer data in a production environment, including backend logic "
                "and deployment."
            ),
            "link": "https://github.com/Bobbykumaar/consumer-data-webapp"
        },
        {
            "title": "IoT-based Crop Management System",
            "description": (
                "Implemented real-time crop monitoring using IoT data and cloud storage, "
                "with intrusion detection to improve farm security and monitoring."
            ),
            "link": "#"
        },
        {
            "title": "Solar Power Optimization & Grid Integration",
            "description": (
                "Implemented the Perturb and Observe algorithm to maximize solar module "
                "output for operating a hydraulic pump, improving system efficiency."
            ),
            "link": "#"
        }
    ]

    experience = [
        {
            "role": "Junior Manager – IT Operations",
            "company": "Intellismart Infrastructure Pvt. Ltd.",
            "duration": "2024 – Present",
            "details": (
                "Part of the IT Operations team managing cloud-based AMISP systems "
                "(HES & MDMS). Automated data collection, report generation, and "
                "analysis using Python. Received the Innovation Award for automating "
                "a critical reporting process in a ₹200+ crore project, reducing "
                "execution time from 12 hours to 4 minutes."
            )
        },
        {
            "role": "Web Development Intern",
            "company": "Microzensys Pvt. Ltd.",
            "duration": "Dec 2022 – Mar 2023",
            "details": (
                "Developed responsive websites using HTML, CSS, JavaScript, and "
                "Bootstrap, gaining hands-on experience in frontend development."
            )
        }
    ]

    return render_template(
        "index.html",
        skills=skills,
        projects=projects,
        experience=experience
    )


if __name__ == "__main__":
    app.run(debug=True)
