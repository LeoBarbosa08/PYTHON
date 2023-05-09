

import os
import re
from pathlib import Path
from unidecode import unidecode

desktop = str(Path.home() / "leo")
print(desktop)

mp3_dir = desktop + '\\mp3\\'
txt_dir = desktop + '\\txt\\'

# Cria os diretórios caso não existam
Path(mp3_dir).mkdir(parents=True, exist_ok=True)
Path(txt_dir).mkdir(parents=True, exist_ok=True)

for filename in os.listdir(mp3_dir):
    if filename.endswith('.mp3'):
        basename = os.path.splitext(filename)[0]
        txt_file = os.path.join(txt_dir, basename + '.txt')
        if os.path.isfile(txt_file):
            with open(txt_file, 'r') as f:
                # Filtra apenas caracteres alfanuméricos do conteúdo do arquivo TXT
                new_name = re.sub(r'[^a-z A-Z 0-9]', '', unidecode(f.read().strip()))
                # Filtra apenas caracteres alfanuméricos do nome do arquivo MP3
                new_name = new_name + '.mp3'
                new_path = os.path.join(mp3_dir, new_name)
                os.rename(os.path.join(mp3_dir, filename), new_path)


