# Script para sorteio de grupos de alunos


### sorteio_grupos.py
Função usada para sorteio de grupos onde:

```
Quantidade de participantes -> qtde_part=34,
Quantidade mínimo por grupo -> qtde_min_grupo=4
```
```py
Retorna:
    { "sorteio": sorteio,               # Lista sorteada
      "total_grupos": total_grupos,     # Qtde de grupos
      "resto": resto,                   # Restante dos participantes (debug)
      "qtde_part": qtde_part,           # Qtde de participantes
      "qtde_min_grupo": qtde_min_grupo, # Qtde mínima no grupo
      "grupos": df_grupos               # DataFrame Pandas dos grupos soteados
    }
``` 

### sorteio_grupos_guipg.py
GUI feita em PySimpleGUIQT para o sorteio dos grupos

> Requerimentos
>```
>Pandas
>PySimpleGUIQt
>```
>```
>pip install pandas PySimpleGUIQt --user
>```
