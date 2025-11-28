from mcp.server.fastmcp import FastMCP
import mysql.connector
from config import db_config

mcp = FastMCP("mcp_mysql")

def conectar():
    conn = mysql.connector.connect(**db_config)
    return conn



@mcp.tool()
def selecciona(sql: str):
    """
    Ejecuta una consulta SELECT en MySQL.
    """
    lower = sql.strip().lower()
    if not lower.startswith("select"):
        raise ValueError("Solo se permiten consultas SELECT en este método.")
    
    conn = conectar()
    cur = conn.cursor(dictionary=True)
    cur.execute(sql)
    rows = cur.fetchall()
    cur.close()
    conn.close()
    return rows

@mcp.tool()
def inserta(sql: str):
    """
    Ejecuta INSERT
    """
    lower = sql.strip().lower()
    if not lower.startswith("insert"):
        raise ValueError("Solo se permiten INSERT.")
    
    conn = conectar()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    affected = cur.rowcount
    cur.close()
    conn.close()
    return {"rows_affected": affected}

@mcp.tool()
def modifica(sql: str):
    """
    Ejecuta UPDATE
    """
    lower = sql.strip().lower()
    if not lower.startswith("update"):
        raise ValueError("Solo se permiten UPDATE")
    
    conn = conectar()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    affected = cur.rowcount
    cur.close()
    conn.close()
    return {"rows_affected": affected}

@mcp.tool()
def elimina(sql: str):
    """
    Ejecuta DELETE.
    """
    lower = sql.strip().lower()
    if not lower.startswith("delete"):
        raise ValueError("Solo se permiten DELETE.")
    
    conn = conectar()
    cur = conn.cursor()
    cur.execute(sql)
    conn.commit()
    affected = cur.rowcount
    cur.close()
    conn.close()
    return {"rows_affected": affected}

@mcp.tool("listar_herramienta")
def listar_herramientas():
    """
    Devuelve todas las herramientas disponibles y su descripción.
    """
    herramientas = {
        "selecciona : Ejecuta una consulta SELECT en MySQL.", 
        "elimina: Ejecuta una consulta DELETE en MySQL.",
        "modifica : Ejecuta una consulta UPDATE en MySQL.",
        "inserta : Ejecuta una consulta INSERT en MySQL."
        
    }
    return herramientas

if __name__ == "__main__":
    mcp.run()