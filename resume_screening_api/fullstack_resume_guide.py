"""
Full Stack Developer Resume Keywords for Better Classification

Add these sections/keywords to your resume to improve classification accuracy:
"""

FULL_STACK_KEYWORDS = {
    "Technical Skills Section": [
        "Full Stack Development",
        "Frontend Development", 
        "Backend Development",
        "MEAN Stack", "MERN Stack", "MEVN Stack",
        "End-to-end Development",
        "Client-server Architecture"
    ],
    
    "Frontend Technologies": [
        "React.js", "Angular", "Vue.js",
        "JavaScript", "TypeScript", "HTML5", "CSS3",
        "Bootstrap", "Tailwind CSS", "Material-UI",
        "Responsive Web Design", "Single Page Applications"
    ],
    
    "Backend Technologies": [
        "Node.js", "Express.js", 
        "Python Django", "Python Flask",
        "RESTful APIs", "GraphQL",
        "Microservices Architecture",
        "API Development", "Server-side Development"
    ],
    
    "Database & DevOps": [
        "MongoDB", "MySQL", "PostgreSQL",
        "Docker", "AWS", "Azure", "Git",
        "CI/CD Pipeline", "Deployment",
        "Cloud Computing", "Version Control"
    ],
    
    "Project Descriptions": [
        "Developed full-stack web applications",
        "Built responsive user interfaces",
        "Designed and implemented REST APIs",
        "Integrated frontend with backend services",
        "Deployed applications to cloud platforms",
        "Collaborated on cross-functional teams"
    ]
}

# Resume Structure Recommendations
RESUME_STRUCTURE = """
RECOMMENDED RESUME STRUCTURE FOR FULL STACK CLASSIFICATION:

1. PROFESSIONAL SUMMARY:
   "Full Stack Developer with X years of experience in modern web development..."

2. TECHNICAL SKILLS:
   Frontend: React.js, JavaScript, HTML5, CSS3...
   Backend: Node.js, Python, Django, REST APIs...
   Database: MongoDB, MySQL, PostgreSQL...
   Tools: Git, Docker, AWS, VS Code...

3. EXPERIENCE:
   - "Developed full-stack web applications using React and Node.js"
   - "Built responsive frontend interfaces with React.js"
   - "Designed RESTful APIs using Express.js/Django"
   - "Integrated frontend components with backend services"

4. PROJECTS:
   - E-commerce Platform (Full Stack)
   - Social Media App (MERN Stack)
   - Portfolio Website (Frontend + Backend)
"""

print("=== FULL STACK RESUME OPTIMIZATION GUIDE ===")
print(RESUME_STRUCTURE)

print("\n=== KEY PHRASES TO INCLUDE ===")
for category, keywords in FULL_STACK_KEYWORDS.items():
    print(f"\n{category}:")
    for keyword in keywords:
        print(f"  ✓ {keyword}")

print("""\n=== IMMEDIATE FIXES FOR YOUR RESUME ===

1. Add "Full Stack Developer" in your title/summary
2. Group skills by Frontend/Backend/Database
3. Use phrases like:
   - "End-to-end web development"
   - "Frontend and backend development" 
   - "Full stack web applications"
   - "Client-server architecture"

4. In project descriptions, mention both frontend AND backend work:
   - "Built frontend using React.js and backend APIs with Python Flask"
   - "Developed full-stack e-commerce platform with user authentication"

5. Include deployment/DevOps keywords:
   - "Deployed to AWS/Heroku/Netlify"
   - "Docker containerization"
   - "CI/CD pipeline setup"
""")
