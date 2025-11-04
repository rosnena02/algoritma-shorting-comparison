"""Simple interactive entrypoint.
Run: python app.py --help
"""
import argparse
from app_fullcomparison_nskip import run_all

parser = argparse.ArgumentParser(description='Run sorting comparison demo.')
parser.add_argument('--mode', choices=['all'], default='all')
args = parser.parse_args()

if args.mode == 'all':
    run_all()
