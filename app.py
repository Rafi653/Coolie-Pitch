"""
Interview Prep Web Application
Flask-based CRUD application for managing interview preparation materials
"""

from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
import os

app = Flask(__name__)
app.config['SECRET_KEY'] = 'dev-secret-key-change-in-production'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///interview_prep.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

# Database Models

class Question(db.Model):
    """Interview Questions"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(50), nullable=False)
    difficulty = db.Column(db.String(20), nullable=False)
    company = db.Column(db.String(100))
    problem = db.Column(db.Text, nullable=False)
    solution = db.Column(db.Text)
    code = db.Column(db.Text)
    time_complexity = db.Column(db.String(50))
    space_complexity = db.Column(db.String(50))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Application(db.Model):
    """Job Applications Tracker"""
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    role = db.Column(db.String(100), nullable=False)
    applied_date = db.Column(db.Date, nullable=False)
    current_stage = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(20), default='Active')
    contact_person = db.Column(db.String(100))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class StudyMaterial(db.Model):
    """Study Materials and References"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    topic = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text)
    source_url = db.Column(db.String(500))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class SyllabusTopic(db.Model):
    """Syllabus Topics Tracker"""
    id = db.Column(db.Integer, primary_key=True)
    topic = db.Column(db.String(200), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    status = db.Column(db.String(20), default='Not Started')
    priority = db.Column(db.String(20), default='Medium')
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class CompanyStyle(db.Model):
    """Company Interview Styles"""
    id = db.Column(db.Integer, primary_key=True)
    company = db.Column(db.String(100), nullable=False)
    rounds = db.Column(db.Integer)
    process_description = db.Column(db.Text)
    tips = db.Column(db.Text)
    common_topics = db.Column(db.String(500))
    timeline = db.Column(db.String(100))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

class Link(db.Model):
    """Useful Links and Resources"""
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    url = db.Column(db.String(500), nullable=False)
    category = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    tags = db.Column(db.String(200))
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

# Routes

@app.route('/')
def index():
    """Home page with dashboard"""
    questions_count = Question.query.count()
    applications_count = Application.query.filter_by(status='Active').count()
    materials_count = StudyMaterial.query.count()
    syllabus_completed = SyllabusTopic.query.filter_by(status='Completed').count()
    syllabus_total = SyllabusTopic.query.count()
    
    recent_applications = Application.query.order_by(Application.updated_at.desc()).limit(5).all()
    
    return render_template('index.html', 
                         questions_count=questions_count,
                         applications_count=applications_count,
                         materials_count=materials_count,
                         syllabus_completed=syllabus_completed,
                         syllabus_total=syllabus_total,
                         recent_applications=recent_applications)

@app.route('/questions')
def questions():
    """List all questions"""
    all_questions = Question.query.order_by(Question.created_at.desc()).all()
    return render_template('questions.html', questions=all_questions)

@app.route('/questions/add', methods=['GET', 'POST'])
def add_question():
    """Add new question"""
    if request.method == 'POST':
        question = Question(
            title=request.form['title'],
            category=request.form['category'],
            difficulty=request.form['difficulty'],
            company=request.form.get('company'),
            problem=request.form['problem'],
            solution=request.form.get('solution'),
            code=request.form.get('code'),
            time_complexity=request.form.get('time_complexity'),
            space_complexity=request.form.get('space_complexity'),
            notes=request.form.get('notes')
        )
        db.session.add(question)
        db.session.commit()
        flash('Question added successfully!', 'success')
        return redirect(url_for('questions'))
    return render_template('add_question.html')

@app.route('/applications')
def applications():
    """List all applications"""
    all_applications = Application.query.order_by(Application.updated_at.desc()).all()
    return render_template('applications.html', applications=all_applications)

@app.route('/applications/add', methods=['GET', 'POST'])
def add_application():
    """Add new application"""
    if request.method == 'POST':
        application = Application(
            company=request.form['company'],
            role=request.form['role'],
            applied_date=datetime.strptime(request.form['applied_date'], '%Y-%m-%d'),
            current_stage=request.form['current_stage'],
            status=request.form.get('status', 'Active'),
            contact_person=request.form.get('contact_person'),
            notes=request.form.get('notes')
        )
        db.session.add(application)
        db.session.commit()
        flash('Application added successfully!', 'success')
        return redirect(url_for('applications'))
    return render_template('add_application.html')

@app.route('/materials')
def materials():
    """List all study materials"""
    all_materials = StudyMaterial.query.order_by(StudyMaterial.created_at.desc()).all()
    return render_template('materials.html', materials=all_materials)

@app.route('/syllabus')
def syllabus():
    """View syllabus progress"""
    all_topics = SyllabusTopic.query.order_by(SyllabusTopic.category, SyllabusTopic.topic).all()
    return render_template('syllabus.html', topics=all_topics)

@app.route('/styles')
def styles():
    """View company interview styles"""
    all_styles = CompanyStyle.query.order_by(CompanyStyle.company).all()
    return render_template('styles.html', styles=all_styles)

@app.route('/links')
def links():
    """View useful links"""
    all_links = Link.query.order_by(Link.category, Link.title).all()
    return render_template('links.html', links=all_links)

# API endpoints for future integrations

@app.route('/api/questions', methods=['GET'])
def api_questions():
    """API endpoint to get all questions"""
    questions = Question.query.all()
    return jsonify([{
        'id': q.id,
        'title': q.title,
        'category': q.category,
        'difficulty': q.difficulty,
        'company': q.company
    } for q in questions])

@app.route('/api/applications', methods=['GET'])
def api_applications():
    """API endpoint to get all applications"""
    applications = Application.query.all()
    return jsonify([{
        'id': a.id,
        'company': a.company,
        'role': a.role,
        'current_stage': a.current_stage,
        'status': a.status
    } for a in applications])

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    # Debug mode should only be enabled during development
    # Set to False in production or use environment variables
    debug_mode = os.environ.get('FLASK_DEBUG', 'False').lower() == 'true'
    app.run(debug=debug_mode)
