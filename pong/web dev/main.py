from flask import Flask, render_template

app = Flask(__name__)

# Sample projects data
projects = [
    {
        'title': 'Personal Website',
        'description': 'A responsive personal website built with HTML, CSS, and JS.',
        'image': 'images/project1.png',
        'link': 'https://github.com/yourusername/personal-website'
    },
    {
        'title': 'Todo App',
        'description': 'A simple Todo app using JavaScript and LocalStorage.',
        'image': 'images/project2.png',
        'link': 'https://github.com/yourusername/todo-app'
    }
]

@app.route('/')
def home():
    return render_template('index.html', projects=projects)

@app.route('/project/<int:project_id>')
def project_detail(project_id):
    project = projects[project_id]
    return render_template('project.html', project=project)

if __name__ == '__main__':
    app.run(debug=True)
