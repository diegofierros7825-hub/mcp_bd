# MCP_BD
Es un mcp (Model Context Protocol) es un estandar abierto para definir como un modelo de IA (Copilot en este caso)
puede conectarse y realizar cambios en una base de datos MySQL

## Caracteristicas
-**Selecciona**: Ejecuta una consulta `SELECT` en MySQL
-**Inserta**: Ejecuta una consulta `INSERT` en MySQL
-**Modifica**: Ejecuta una consulta `UPDATE` en MySQL
-**Elimina**: Ejecuta una consulta `DELETE` en MySQL
-**Listar_herramientas**: Devuelve todas las herramientas disponibles 

## Instalación 
```bash
# Clonar repositorio
git clone https://github.com/diegofierros7825-hub/mcp_bd.git

# Entrar al proyecto
cd mcp_bd

# (Opcional) Crear un entorno virtual
python -m venv venv
venv\Scripts\activate
```
## Instalar dependencias
```bash
pip install "mcp[cli]"
pip install mysql.connector

```
## Uso
```bash
mcp run .\mcp_BD.py -t sse
```

```bash
📦 mcp_bd
├── .vscode
│ ├── mcp.json
├── README.md
├── config.py
└── mcp_BD.py
```
