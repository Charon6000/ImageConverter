import os
from PIL import Image
import click

@click.command()
@click.option('--dir', 'dir', help='Directory of files', required=True)
@click.option('--exten', 'extenction', help='Extenction of files', required=False, default="png")

def zmiana_nazwy(dir:str, extenction:str):
    a=0
    for file_path in os.listdir(dir):
        a+=1
        im = Image.open(f"{dir}/{file_path}")
        rgb_im = im.convert("RGB")
        os.remove(f"{dir}/{file_path}")
        file = file_path.split(".")
        txt =""
        if len(file_path) == 1:
            rgb_im.save(f"{dir}/{file[0]}{extenction}")
            print(f"[{a}/{len(os.listdir(dir))}] Converted {file_path} to {file[0]}{extenction}")
        else:
            for f in range(0,len(file)-1):
                txt +=f"{file[f]}."
            rgb_im.save(f"{dir}/{txt}{extenction}")
            print(f"[{a}/{len(os.listdir(dir))}] Converted {file_path} to {txt}{extenction}")

zmiana_nazwy()
