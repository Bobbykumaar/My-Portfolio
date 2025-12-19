from flask import Flask, render_template, url_for

app = Flask(__name__)

@app.route('/')
def home():
    # Projects
    projects = [
        {
            'title': 'Consumer Data Web App',
            'description': 'Built a Flask backend with MongoDB for managing production-level data.',
            'link': 'https://github.com/Bobbykumaar/consumer-data-webapp'
        },
        {
            'title': 'IoT-based Crop Management',
            'description': 'Real-time crop monitoring using IoT data, cloud storage, and intrusion detection.',
            'link': '#'
        },
        {
            'title': 'Solar Power Optimization & Grid Integration',
            'description': 'Implemented Perturb and Observe algorithm to maximize solar output for a hydraulic pump.',
            'link': '#'
        }
    ]
    
    # Skills
    skills = [
        'Python Programming',
        'Data Analysis & Automation (Pandas, NumPy, Selenium)',
        'Web Development (Flask, HTML, CSS, JS)',
        'Electrical & Control Systems',
        'Cloud-based AMISP systems (HES & MDMS)',
        'Project & Vendor Management'
    ]

    # Experience
    experience = [
        {
            'role': 'Junior Manager – IT Operations',
            'company': 'Intellismart Infrastructure Pvt. Ltd.',
            'duration': '2024 – Present',
            'details': 'Worked on Python automation, cloud-based AMISP systems, and received Innovation Award.'
        },
        {
            'role': 'Web Development Intern',
            'company': 'Microzensys Pvt. Ltd.',
            'duration': 'Dec 2022 – Mar 2023',
            'details': 'Developed responsive websites using HTML, CSS, JS, Bootstrap.'
        }
    ]
    
    return render_template('index.html', projects=projects, skills=skills, experience=experience)

if __name__ == '__main__':
    app.run(debug=True)
