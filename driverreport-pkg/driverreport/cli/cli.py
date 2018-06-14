"""
MODULE: cli.cli.py
DESCRIPTION: CLI wrapper using Google's fire module
"""
from __future__ import absolute_import
import fire
from ..core import main

class Pipeline(object):
    """Main pipeline for fire cli commands"""
    def run(self, path):
       print main.driver_report(path)

def _main():
    """Wrapper for main fire cli caller"""
    fire.Fire(Pipeline)

if __name__ == '__main__':
    _main()