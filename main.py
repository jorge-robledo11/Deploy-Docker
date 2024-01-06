import pandas as pd
import numpy as np
import sqlite3
import smtplib
import os
from faker import Faker
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from dotenv import load_dotenv
load_dotenv()

# Variables de entorno
sender_email = os.getenv('SENDER_EMAIL')
receiver_email = os.getenv('RECEIVER_EMAIL')
password = os.getenv('PASSWORD')


def create_random_data(num_rows):
    
    fake = Faker()
    np.random.seed(0)  # Para reproducibilidad
    
    data = {
        'ID': [fake.unique.random_number(digits=8) for _ in range(num_rows)],
        'Country': [fake.country() for _ in range(num_rows)],
        'Credit_Limit': [np.random.randint(1000, 10000) for _ in range(num_rows)],
        'Credit_Card_Name': [fake.credit_card_provider() for _ in range(num_rows)],
        'Gender': [fake.random_element(elements=('Male', 'Female')) for _ in range(num_rows)],
        'Occupation': [fake.job() for _ in range(num_rows)],
        'Marital_Status': [fake.random_element(elements=('Single', 'Married', 'Divorced', 'Widowed')) for _ in range(num_rows)]
    }
    return pd.DataFrame(data)


def send_email(html):
    message = MIMEMultipart()
    message['From'] = sender_email
    message['To'] = receiver_email
    message['Subject'] = 'Resultado de la Consulta SQL'

    # Adjuntar el DataFrame como HTML
    message.attach(MIMEText(html, 'html'))

    # Configuración del servidor SMTP y envío del correo
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
    server.quit()
    

# ==============================================================================    

def main():
    
    df = create_random_data(3000)

    # Conectar a una base de datos SQLite en memoria
    conn = sqlite3.connect(':memory:')

    # Escribir el DataFrame a la base de datos como una tabla
    df.to_sql('credit_data', conn, index=False, if_exists='replace')

    # Ejecutar consulta SQL
    query = """
    SELECT * 
    FROM credit_data 
    WHERE Credit_Limit > 5000
    """
    result = pd.read_sql_query(query, conn)

    # Cerrar la conexión
    conn.close()

    # Convertir el DataFrame a HTML
    html = result.to_html(index=False)
    
    # Enviar el resultado por correo electrónico
    send_email(html)

if __name__ == '__main__':
    main()
