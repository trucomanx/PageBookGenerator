#!/usr/bin/python3

import shutil
import json
import os 

def gerar_html_de_template(template_path, saida_path, textos):
    """
    Lê um template HTML e substitui placeholders {{CHAVE}}
    pelos valores do dict.
    """

    # Lê template
    with open(template_path, "r", encoding="utf-8") as f:
        conteudo = f.read()

    # Substitui placeholders
    for chave, valor in textos.items():
        placeholder = "{{" + chave + "}}"
        conteudo = conteudo.replace(placeholder, valor)

    # Salva arquivo final
    with open(saida_path, "w", encoding="utf-8") as f:
        f.write(conteudo)

    print(f"Arquivo gerado: {saida_path}")


def working_templates(input_dir, output_dir, footer_header, index_data, index_src):
    os.makedirs(output_dir,exist_ok=True)
   
    gerar_html_de_template(
        os.path.join(input_dir,"head.html"),
        os.path.join(output_dir,"head.html"),
        footer_header
    )
    
    gerar_html_de_template(
        os.path.join(input_dir,"foot.html"),
        os.path.join(output_dir,"foot.html"),
        footer_header
    )

    gerar_html_de_template(
        os.path.join(input_dir, index_src),
        os.path.join(output_dir,"index.html"),
        index_data
    )

def pipeline(   index_data_path,
                description_path,
                bibliography_path,
                language = "pt",
                output_dir="output"):    
    
    dir_of_file = os.path.dirname(os.path.abspath(__file__))
    input_dir = os.path.join(dir_of_file, "templates")
    
    with open(os.path.join(input_dir, f"footer_header_{language}.json"), "r", encoding="utf-8") as f:
        footer_header = json.load(f)
        
    with open(index_data_path, "r", encoding="utf-8") as f:
        index_data = json.load(f)

    bibliography = ""
    if os.path.exists(bibliography_path):
        with open(bibliography_path, "r", encoding="utf-8") as f:
            bibliography = f.read()
        
    with open(description_path, "r", encoding="utf-8") as f:
        description = f.read()

    os.makedirs(output_dir,exist_ok=True)
    
    index_data["description"] = description
    index_data["bibtex"] = bibliography
    
    footer_header["email-link"] = index_data["email-link"]
    footer_header["bug-link"] = index_data["bug-link"]
    footer_header["x-link"] = index_data["x-link"]
    footer_header["youtube-link"] = index_data["youtube-link"]
    footer_header["rss-link"] = index_data["rss-link"]

    shutil.copytree(os.path.join(input_dir,"images"), 
                    os.path.join(output_dir,"images"),
                    dirs_exist_ok=True)
    
    shutil.copytree(os.path.join(input_dir,"data"), 
                    os.path.join(output_dir,"data"),
                    dirs_exist_ok=True)

    if os.path.exists(bibliography_path):
        shutil.copy(bibliography_path, os.path.join(output_dir,"data","bibliography.bib"))
                    
    working_templates(input_dir, output_dir, footer_header, index_data, f"index_{language}.html")

def main(): 
    language = "pt"
    index_data_path = "index_data.json"
    description_path = "description.txt"
    bibliography_path = "bibliography.bib"
    
    output_dir="output"
    
    pipeline(   index_data_path,
                description_path,
                bibliography_path,
                language,
                output_dir)

if __name__ == "__main__":
    main()
    
