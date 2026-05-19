#!/usr/bin/python3

import argparse
import shutil
import os

import page_book_generator.about as about

from page_book_generator.worker import pipeline
from page_book_generator.modules.wabout import show_about

class AboutAction(argparse.Action):
    def __call__(self, parser, namespace, values, option_string=None):
        show_about()
        parser.exit()

def main():

    parser = argparse.ArgumentParser(
        prog=about.__program_name__,
        description=about.__description__,
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )

    parser.add_argument(
        "--about",
        nargs=0,
        action=AboutAction,
        help="Show information about the application"
    )

    LANGUAGES = ["pt", "en"]
    parser.add_argument(
        "--language",
        type=str,
        required=True,
        choices=LANGUAGES,
        default=LANGUAGES[0],
        help="Language"
    )

    parser.add_argument(
        "--index-data",
        type=str,
        required=True,
        help="JSON file with index data"
    )

    parser.add_argument(
        "--description",
        type=str,
        required=True,
        help="Description file"
    )

    parser.add_argument(
        "--bibliography",
        type=str,
        default="",
        help="BibTex file *.bib."
    )
    
    parser.add_argument(
        "--screenshot1",
        type=str,
        default="",
        help="Source path of first PNG screenshot. Only PNG is supported."
    )
    
    parser.add_argument(
        "--screenshot2",
        type=str,
        default="",
        help="Source path of second PNG screenshot. Only PNG is supported."
    )
    
    parser.add_argument(
        "--cover",
        type=str,
        default="",
        help="Source path of second PNG screenshot. Only PNG is supported."
    )

    TEMPLATE_TYPES = ["complete", "print-only"]
    parser.add_argument(
        "--template-type",
        type=str,
        choices=TEMPLATE_TYPES,
        default=TEMPLATE_TYPES[0],
        help="Type of template"
    )
    
    parser.add_argument(
        "--output-dir",
        type=str,
        default="output",
        help="Output directory"
    )

    args = parser.parse_args()

    pipeline(
        args.index_data,
        args.description,
        args.bibliography,
        args.language,
        args.template_type,
        args.output_dir
    )
    
    if os.path.exists(args.screenshot1):
        shutil.copy(args.screenshot1, os.path.join(args.output_dir,"images","screenshot1.png"))
    
    if os.path.exists(args.screenshot2):
        shutil.copy(args.screenshot2, os.path.join(args.output_dir,"images","screenshot2.png"))
        
    if os.path.exists(args.cover):
        shutil.copy(args.cover, os.path.join(args.output_dir,"images","cover.png"))

    #show_about()



if __name__ == "__main__":
    main()
