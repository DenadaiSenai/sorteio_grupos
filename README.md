# Script para sorteio de grupos de alunos

Funçao usada para sorteio de grupos onde:

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
