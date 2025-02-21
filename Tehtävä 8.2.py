import mysql.connector

# Yhdistetään ilman tietokannan nimeä
yhteys = mysql.connector.connect(
    host='127.0.0.1',
    port=3306,
    user='root',
    password='Karim88',
    collation='utf8_general_ci',
    autocommit=True
)

# Luodaan tietokanta
kursori = yhteys.cursor()
kursori.execute("CREATE DATABASE IF NOT EXISTS flight_game")
print("Tietokanta luotu onnistuneesti!")
kursori.close()
yhteys.close()
