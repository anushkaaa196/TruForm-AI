#!/usr/bin/env python3
"""
AI Biomechanics & Posture Analyzer
Main Application Entry Point.
"""

from database.db_manager import init_db
from ui.app import run_app

if __name__ == "__main__":
    init_db()
    run_app(require_auth=True)

