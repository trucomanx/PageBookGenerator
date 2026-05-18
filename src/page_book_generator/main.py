#!/usr/bin/python3

import argparse

from worker import pipeline


def main():

    parser = argparse.ArgumentParser(
        description="Gerador de páginas HTML"
    )

    parser.add_argument(
        "--language",
        required=True,
        help="Idioma (ex: pt, en)"
    )

    parser.add_argument(
        "--index-data",
        required=True,
        help="Arquivo JSON com dados do index"
    )

    parser.add_argument(
        "--description",
        required=True,
        help="Arquivo de descrição"
    )

    parser.add_argument(
        "--bibliography",
        required=True,
        help="Arquivo bibliography.bib"
    )

    parser.add_argument(
        "--output-dir",
        default="output",
        help="Diretório de saída"
    )

    args = parser.parse_args()

    pipeline(
        args.index_data,
        args.description,
        args.bibliography,
        args.language,
        args.output_dir
    )


if __name__ == "__main__":
    main()
