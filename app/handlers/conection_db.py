import mysql.connector

def conection():
    db = mysql.connector.connect(
        host ="localhost",
        user ="root",
        passwd ="",
        database = "flask-sc"
        )
    return db