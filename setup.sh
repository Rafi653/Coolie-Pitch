#!/bin/bash

# Interview Prep Webapp - Quick Start Script

echo "🎯 Interview Prep Webapp - Setup"
echo "================================="
echo ""

# Check Python version
echo "Checking Python installation..."
python3 --version || python --version

# Create virtual environment if it doesn't exist
if [ ! -d "venv" ]; then
    echo ""
    echo "Creating virtual environment..."
    python3 -m venv venv || python -m venv venv
fi

# Activate virtual environment
echo ""
echo "Activating virtual environment..."
if [ -f "venv/bin/activate" ]; then
    source venv/bin/activate
elif [ -f "venv/Scripts/activate" ]; then
    source venv/Scripts/activate
fi

# Install requirements
echo ""
echo "Installing dependencies..."
pip install -r requirements.txt

# Initialize database
echo ""
echo "Initializing database..."
python app.py &
APP_PID=$!
sleep 3
kill $APP_PID 2>/dev/null

echo ""
echo "✅ Setup complete!"
echo ""
echo "To start the application:"
echo "  1. Activate virtual environment:"
echo "     source venv/bin/activate  (Linux/Mac)"
echo "     venv\\Scripts\\activate     (Windows)"
echo ""
echo "  2. Run the application:"
echo "     python app.py"
echo ""
echo "  3. Open browser to: http://127.0.0.1:5000"
echo ""
echo "Happy interview prepping! 🚀"
