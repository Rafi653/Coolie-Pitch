# Interview Prep Webapp 🎯

A personal web application for managing interview preparation materials, tracking job applications, and organizing study plans for Big Tech/FAANG interviews. Specifically designed for mid-level data engineers and backend developers.

## 🚀 Features

- **Practice Questions**: Store and organize coding, system design, behavioral, and data engineering questions with solutions
- **Job Applications Tracker**: Monitor application status, interview stages, and feedback across multiple companies
- **Study Materials**: Curate reference articles, summaries, and learning resources organized by topic
- **Syllabus Management**: Track progress on interview prep topics with a comprehensive checklist
- **Company Interview Styles**: Document interview processes and tips for different companies
- **Resource Links**: Maintain a collection of useful preparation resources and bookmarks
- **Web-based CRUD Interface**: Flask-powered UI for easy content management

## 📁 Repository Structure

```
Coolie-Pitch/
├── app.py                      # Main Flask application
├── requirements.txt            # Python dependencies
├── .gitignore                 # Git ignore file
├── README.md                  # This file
│
├── app/                       # Application code
│   ├── static/
│   │   ├── css/
│   │   │   └── style.css     # Application styles
│   │   └── js/               # JavaScript (future)
│   └── templates/            # HTML templates
│       ├── base.html
│       ├── index.html
│       ├── questions.html
│       ├── add_question.html
│       ├── applications.html
│       ├── add_application.html
│       ├── materials.html
│       ├── syllabus.html
│       ├── styles.html
│       └── links.html
│
├── data/                      # Database storage
│   └── interview_prep.db     # SQLite database (auto-generated)
│
├── material/                  # Study material and references
│   └── README.md             # Structure guide
│
├── questions/                 # Practice questions (markdown)
│   └── README.md             # Format guide
│
├── applications/              # Job application tracking data
│   └── README.md             # Tracking guide
│
├── syllabus/                  # Interview prep syllabus
│   └── README.md             # Topic checklist
│
├── styles/                    # Company interview processes
│   └── README.md             # Documentation guide
│
└── links/                     # Useful resources
    └── README.md             # Link categories
```

## 🛠️ Setup Instructions

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)

### Installation

1. **Clone the repository**:
   ```bash
   git clone https://github.com/Rafi653/Coolie-Pitch.git
   cd Coolie-Pitch
   ```

2. **Create a virtual environment** (recommended):
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

4. **Initialize the database**:
   ```bash
   python app.py
   ```
   The database will be automatically created on first run.

5. **Access the application**:
   Open your browser and navigate to: `http://127.0.0.1:5000`

### Development Mode

For development with debug mode enabled:
```bash
FLASK_DEBUG=true python app.py
```

**⚠️ Security Note**: Debug mode should **NEVER** be enabled in production as it allows arbitrary code execution. By default, debug mode is disabled.

## 📖 Usage Guide

### Web Application

The Flask web app provides a user-friendly interface for all operations:

- **Dashboard**: Overview of your preparation progress with quick stats
- **Questions**: Add, view, and manage practice interview questions
- **Applications**: Track job applications and interview stages
- **Materials**: Browse study materials (web UI + file-based)
- **Syllabus**: Monitor topic coverage and progress
- **Company Styles**: Reference company-specific interview processes
- **Links**: Access your curated collection of resources

### Adding Content

#### Via Web Interface
1. Navigate to the relevant section (Questions, Applications, etc.)
2. Click the "Add" button
3. Fill in the form and submit

#### Via File System
You can also add content directly to the folders:

- **Study Materials**: Add markdown files to `material/` organized by topic
- **Question Bank**: Add markdown files to `questions/` using the template
- **Company Guides**: Add markdown files to `styles/` for each company

### Database vs File System

- **Database**: Questions, Applications, Syllabus progress (use web UI)
- **Files**: Study materials, company guides, markdown references

## 🎯 Content Organization

### For Data Engineers / Backend Developers

#### Key Areas to Focus On:

1. **Data Structures & Algorithms**
   - Arrays, linked lists, trees, graphs, hash tables
   - Sorting, searching, dynamic programming
   - Time and space complexity analysis

2. **System Design**
   - Scalability, load balancing, caching
   - Database design (SQL vs NoSQL)
   - Distributed systems, microservices
   - Message queues, stream processing

3. **Data Engineering**
   - ETL/ELT pipeline design
   - Data warehousing and modeling
   - Apache Spark, Kafka, Airflow
   - Data quality and governance

4. **Backend Development**
   - API design and development
   - Database optimization
   - Testing and CI/CD
   - Cloud platforms (AWS/GCP/Azure)

5. **Behavioral**
   - Leadership principles
   - Project deep dives using STAR method
   - Conflict resolution examples

## 🔮 Future Enhancements

- [ ] Web scraping scripts for automated content updates
  - LeetCode problems
  - Company interview experiences from Glassdoor/Blind
  - Latest system design articles
- [ ] Progress analytics and visualizations
- [ ] Spaced repetition for question review
- [ ] Mock interview timer and recorder
- [ ] Integration with external APIs (LeetCode, GitHub)
- [ ] Export functionality (PDF, markdown)
- [ ] Mobile-responsive improvements

## 🤝 Contributing

This is a personal project, but feel free to fork and adapt for your own use!

## 📄 License

This project is for personal use. Feel free to use and modify for your interview preparation.

## 🎓 Resources

Check the `links/README.md` for curated resources, or visit the Links section in the web app.

---

**Good luck with your interviews! 🚀**