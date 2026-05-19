SKILLS = [
    "python",
    "sql",
    "machine learning",
    "deep learning",
    "tensorflow",
    "pytorch",
    "fastapi",
    "docker",
    "aws",
    "react",
    "nlp",
    "pandas",
    "numpy",
    "scikit-learn",
    "flask",
    "git",
    "opencv"
]

def extract_skill(text):
    found_skill = []

    text = text.lower()

    for skill in SKILLS:
        if skill in text:
            found_skill.append(skill)

    return list(set(found_skill))

# ROLE_SKILLS = {

#     "Operations Manager": [
#         "Operations Management",
#         "Project Management",
#         "Leadership",
#         "Team Management",
#         "Strategic Planning",
#         "Communication",
#         "Business Operations",
#         "Problem Solving",
#         "Microsoft Excel",
#         "Process Improvement"
#     ],

#     "Testing": [
#         "Manual Testing",
#         "Test Cases",
#         "Bug Tracking",
#         "Selenium",
#         "Automation Testing",
#         "JIRA",
#         "API Testing",
#         "Regression Testing",
#         "SQL",
#         "Agile"
#     ],

#     "Web Designing": [
#         "HTML",
#         "CSS",
#         "JavaScript",
#         "Bootstrap",
#         "React",
#         "UI/UX Design",
#         "Responsive Design",
#         "Figma",
#         "Adobe XD",
#         "Git"
#     ],

#     "Python Developer": [
#         "Python",
#         "Django",
#         "Flask",
#         "FastAPI",
#         "REST API",
#         "SQL",
#         "Git",
#         "Docker",
#         "Problem Solving",
#         "Data Structures"
#     ],

#     "Data Science": [
#         "Python",
#         "Machine Learning",
#         "Deep Learning",
#         "SQL",
#         "Pandas",
#         "NumPy",
#         "Statistics",
#         "Data Visualization",
#         "Scikit-learn",
#         "Power BI"
#     ],

#     "Business Analyst": [
#         "Business Analysis",
#         "SQL",
#         "Excel",
#         "Power BI",
#         "Data Analysis",
#         "Communication",
#         "Requirement Gathering",
#         "Stakeholder Management",
#         "Reporting",
#         "Problem Solving"
#     ],

#     "Civil Engineer": [
#         "AutoCAD",
#         "Civil Engineering",
#         "Site Management",
#         "Construction Management",
#         "Project Planning",
#         "Structural Design",
#         "Surveying",
#         "Safety Standards",
#         "Quantity Estimation",
#         "Problem Solving"
#     ],

#     "PMO": [
#         "Project Management",
#         "PMO",
#         "Risk Management",
#         "Scheduling",
#         "Budget Management",
#         "Leadership",
#         "Communication",
#         "Documentation",
#         "Agile",
#         "Stakeholder Management"
#     ],

#     "Electrical Engineering": [
#         "Electrical Engineering",
#         "Circuit Design",
#         "PLC",
#         "AutoCAD",
#         "MATLAB",
#         "Power Systems",
#         "Troubleshooting",
#         "Control Systems",
#         "Electrical Maintenance",
#         "Problem Solving"
#     ],

#     "Sales": [
#         "Sales",
#         "Negotiation",
#         "Communication",
#         "Lead Generation",
#         "CRM",
#         "Customer Relationship",
#         "Marketing",
#         "Presentation Skills",
#         "Business Development",
#         "Teamwork"
#     ],

#     "Database": [
#         "SQL",
#         "MySQL",
#         "PostgreSQL",
#         "Oracle",
#         "Database Management",
#         "Query Optimization",
#         "Data Modeling",
#         "Backup and Recovery",
#         "Performance Tuning",
#         "PL/SQL"
#     ],

#     "ETL Developer": [
#         "ETL",
#         "Informatica",
#         "SQL",
#         "Data Warehousing",
#         "Python",
#         "SSIS",
#         "Data Integration",
#         "Oracle",
#         "Data Migration",
#         "Problem Solving"
#     ],

#     "Arts": [
#         "Creativity",
#         "Communication",
#         "Design Thinking",
#         "Presentation Skills",
#         "Adobe Photoshop",
#         "Illustrator",
#         "Content Creation",
#         "Critical Thinking",
#         "Teamwork",
#         "Time Management"
#     ],

#     "DotNet Developer": [
#         "C#",
#         ".NET",
#         "ASP.NET",
#         "MVC",
#         "SQL Server",
#         "REST API",
#         "Entity Framework",
#         "JavaScript",
#         "Git",
#         "Problem Solving"
#     ],

#     "SAP Developer": [
#         "SAP",
#         "ABAP",
#         "SAP HANA",
#         "SQL",
#         "ERP",
#         "SAP Modules",
#         "Data Migration",
#         "Problem Solving",
#         "Business Processes",
#         "Communication"
#     ],

#     "Health and fitness": [
#         "Fitness Training",
#         "Nutrition",
#         "Communication",
#         "Health Coaching",
#         "Workout Planning",
#         "Client Management",
#         "Leadership",
#         "Motivation",
#         "CPR",
#         "Wellness"
#     ],

#     "Java Developer": [
#         "Java",
#         "Spring Boot",
#         "Hibernate",
#         "REST API",
#         "MySQL",
#         "Microservices",
#         "Git",
#         "Maven",
#         "Problem Solving",
#         "Data Structures"
#     ],

#     "Blockchain": [
#         "Blockchain",
#         "Solidity",
#         "Ethereum",
#         "Smart Contracts",
#         "Web3",
#         "Cryptography",
#         "JavaScript",
#         "Node.js",
#         "Git",
#         "Problem Solving"
#     ],

#     "Advocate": [
#         "Legal Research",
#         "Communication",
#         "Documentation",
#         "Contract Law",
#         "Court Proceedings",
#         "Negotiation",
#         "Legal Drafting",
#         "Problem Solving",
#         "Compliance",
#         "Client Handling"
#     ],

#     "HR": [
#         "Recruitment",
#         "Communication",
#         "Employee Relations",
#         "HR Management",
#         "Talent Acquisition",
#         "Payroll",
#         "Leadership",
#         "Conflict Resolution",
#         "MS Excel",
#         "Onboarding"
#     ],

#     "Mechanical Engineer": [
#         "Mechanical Engineering",
#         "AutoCAD",
#         "SolidWorks",
#         "Manufacturing",
#         "Thermodynamics",
#         "Project Management",
#         "Maintenance",
#         "Problem Solving",
#         "Quality Control",
#         "Machine Design"
#     ],

#     "Network Security Engineer": [
#         "Cyber Security",
#         "Network Security",
#         "Firewall",
#         "Linux",
#         "Penetration Testing",
#         "SIEM",
#         "Risk Assessment",
#         "Cryptography",
#         "Incident Response",
#         "Python"
#     ],

#     "Automation Testing": [
#         "Selenium",
#         "Automation Testing",
#         "Java",
#         "Python",
#         "TestNG",
#         "API Testing",
#         "JIRA",
#         "Manual Testing",
#         "CI/CD",
#         "SQL"
#     ],

#     "Hadoop": [
#         "Hadoop",
#         "Hive",
#         "Spark",
#         "HDFS",
#         "Big Data",
#         "Scala",
#         "Kafka",
#         "SQL",
#         "Data Processing",
#         "Linux"
#     ],

#     "DevOps Engineer": [
#         "Docker",
#         "Kubernetes",
#         "AWS",
#         "CI/CD",
#         "Jenkins",
#         "Linux",
#         "Terraform",
#         "Git",
#         "Monitoring",
#         "Shell Scripting"
#     ]
# }