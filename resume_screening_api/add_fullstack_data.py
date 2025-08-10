# Add these full-stack sample resumes to your dataset

full_stack_samples = [
    {
        "Category": "Full Stack Developer",
        "Resume": """Full Stack Developer with 3 years experience in MEAN/MERN stack. 
        Frontend: React.js, Angular, Vue.js, HTML5, CSS3, JavaScript, TypeScript, Bootstrap, Tailwind CSS
        Backend: Node.js, Express.js, Python, Django, Flask, REST APIs, GraphQL
        Database: MongoDB, MySQL, PostgreSQL, Redis
        Cloud: AWS, Azure, Docker, Kubernetes, CI/CD
        Tools: Git, Webpack, npm, yarn, Jest, Cypress
        Experience: Built e-commerce platforms, social media apps, and dashboard applications"""
    },
    {
        "Category": "Full Stack Developer", 
        "Resume": """Experienced Full Stack Web Developer specializing in React and Python.
        Frontend Technologies: React.js, Redux, JavaScript ES6+, HTML5, CSS3, SASS, Material-UI
        Backend Technologies: Python, Django, Flask, Node.js, Express.js, RESTful APIs
        Database: PostgreSQL, MongoDB, MySQL, SQLite
        DevOps: Docker, AWS EC2, S3, Heroku deployment, GitHub Actions
        Projects: Developed full-stack web applications with user authentication, payment integration, and real-time features"""
    },
    {
        "Category": "Full Stack Developer",
        "Resume": """Full Stack Software Engineer with expertise in modern web development.
        Frontend: Vue.js, React, Angular, TypeScript, JavaScript, HTML, CSS, Bootstrap
        Backend: Python Django, Node.js, Java Spring Boot, PHP Laravel
        Database: MySQL, PostgreSQL, MongoDB, Firebase
        Cloud Services: AWS, Google Cloud, Azure, Docker containers
        Tools: Git, Webpack, npm, Jest testing, Agile methodologies
        Built responsive web applications, microservices architecture, and API integrations"""
    }
]

import pandas as pd

# Read existing dataset
df = pd.read_csv('../resume_dataset.csv')
print(f"Original dataset size: {len(df)}")

# Add full stack samples
for sample in full_stack_samples:
    new_row = pd.DataFrame([sample])
    df = pd.concat([df, new_row], ignore_index=True)

print(f"New dataset size: {len(df)}")

# Save updated dataset
df.to_csv('../resume_dataset_updated.csv', index=False)
print("Updated dataset saved as 'resume_dataset_updated.csv'")

# Show category counts
print("\nCategory distribution:")
print(df['Category'].value_counts().head(10))
