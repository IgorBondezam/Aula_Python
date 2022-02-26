"""
Módulos padrao do python:
módulos são arquivos .py (que contém código python) e servem para expandir as funcionalidades padrão da linguagem.
Veja todos os módulos padão do python em:
https://docs.python.org/3/py-modindex.html
"""
from sys import platform as so  # modulo sys SOMENTE a funcão platform como apelido so

print(so)

import random  #  Estamos importandoTODO o random

print(random.randint(0, 10))
