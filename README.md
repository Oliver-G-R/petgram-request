# Script en python para generar datos en Petgram

Actualmente solo se pueden crear usuarios, la información se genera gracias al modulo faker,  
y sus campos necesarios para cada request.

## Inicio  

```bash
  pip install -r requirements.txt
  python src/index.py
```

### Argumentos   
- Puedes pasar una cantidad de veces por request:   **--n cantidad**  
- El tipo de request **--type {post, user}** (Actualmente solo disponible User)  


## Datos  
Para generar datos puedes usar el archivo data.py y crear una función con los campos  
adecuados. 