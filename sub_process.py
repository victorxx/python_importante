from pathlib import Path
import subprocess
import random
import time

scripts = [
    r"C:\Users\vitor\Desktop\bots\divulgar_grupo.py",
]

for caminho in scripts:
    caminhos = Path(caminho)
    
    subprocess.run(
        ["python", str(caminhos)],
        check=True
    )
    
    print("ok ta tudo certo")
