# esta es una prueba de desarrollo de una API para envío de correos electrónicos con Azure Communication Services, ejemplo test.py

import os
from dotenv import load_dotenv

# Carga las variable de entorno desde el archivo .env
load_dotenv()

from azure.communication.email import EmailClient
from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route("/send-email", methods=["POST"])
def send_email():
    try:
        connection_string = os.environ.get("CONNECTION_STRING")
        client = EmailClient.from_connection_string(connection_string)

        data = request.get_json()
        email = data["email"]
        subject = data.get("subject", "Código de seguridad")  # Usa un valor predeterminado si no se proporciona
        body = data.get("body", "Hola, este es su código.")  # Usa un valor predeterminado si no se proporciona


        message = {
            "senderAddress": os.environ.get("SENDER_ADDRESS"),
            "recipients": {
                "to": [{"address": email}],
            },
            "content": {
                # "subject": data.get("subject", "Código de seguridad"), 
                # "plainText": data.get("body", "Hola, este es su código."), 
                "subject": subject,
                "plainText": body,
           
            },
        }

        poller = client.begin_send(message)
        result = poller.result()

        return jsonify({"message": "Email sent successfully"}), 200

    except Exception as ex:
        return jsonify({"message": str(ex)})


if __name__ == "__main__":
    app.run(debug=True)
