#!/usr/bin/env python3
"""Validate the ENGSE206 team repository and weekly submission support.
Run: python3 scripts/check-project-structure.py
Optional: python3 scripts/check-project-structure.py --week 3
"""
from pathlib import Path
import argparse, sys

root = Path(__file__).resolve().parents[1]
weeks = [1,2,3,4,5,6,7,8,10,11,12,13,14,15,16]
required = [
    'README.md','TEAM.md','CASE_CARD.md','COURSE_REPOSITORY.md',
    'STUDENT_SUBMISSION_GUIDE.md','PROJECT_STATUS.md',
    'project-management/team-worklog.md','project-management/ai-use-log.md',
    'project-management/course-sync-log.md','project-management/weekly-status.md',
    'submissions/submission-register.md','final/README.md'
]
required += [f'submissions/week-{w:02d}-submission.md' for w in weeks]

parser=argparse.ArgumentParser()
parser.add_argument('--week',type=int,choices=weeks)
args=parser.parse_args()

paths=required
if args.week:
    paths=[f'submissions/week-{args.week:02d}-submission.md','submissions/submission-register.md','project-management/team-worklog.md']
missing=[p for p in paths if not (root/p).exists()]
if missing:
    print('FAIL: missing required files')
    for p in missing: print(' -',p)
    sys.exit(1)
print('PASS:', 'Week '+str(args.week) if args.week else 'repository', 'structure is ready.')
