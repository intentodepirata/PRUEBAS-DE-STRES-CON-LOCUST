# TEST DE STRES

## Instalar dependendcias

```
pip install -r requirements.txt
```

## Ejecutar App

Abre la terminal y escribe

```bash
locust -f main.py
```

## Ejecutar prueba

Al ejecutar la app se te abrira una ventana del navegador en la direccion http://localhost:8089

1 - Tendras que configurar desde la web 3 opciones y pulsar en start swarming

- Number of users (peak concurrency)
- Spawn rate (users started/second)
- Host (e.g. http://www.example.com)
