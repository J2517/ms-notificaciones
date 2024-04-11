from azure.communication.email import EmailClient


def main():
    try:
        connection_string = "endpoint=https://jackeline-progiii.unitedstates.communication.azure.com/;accesskey=zAuPnAaSasn63n9NgkpybAxlY90mrP/gd3OqDEkHHI2DBrdr9Xgm69PelnQd2FbUNf1XnO0EgYBFT7jJnhpDog=="
        client = EmailClient.from_connection_string(connection_string)

        message = {
            "senderAddress": "DoNotReply@91ab8e02-6d22-4089-b5c2-78e8c0eeb469.azurecomm.net",
            "recipients": {
                "to": [{"address": "jackria345@gmail.com"}],
            },
            "content": {
                "subject": "prueba",
                "plainText": "Hola este es desde acá.",
            },
        }

        poller = client.begin_send(message)
        result = poller.result()

    except Exception as ex:
        print(ex)


main()
