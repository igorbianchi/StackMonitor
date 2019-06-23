import time
import zmq
import random

acoes = {"PETR4": {"nome": "PETR4", "valor": 10}, "VALE3": {"nome": "VALE3", "valor": 10},
         "ITUB4": {"nome": "ITUB4", "valor": 10}, "B3SA3": {"nome": "B3SA3", "valor": 10},
         "BBAS3": {"nome": "BBAS3", "valor": 10}, "BBDC4": {"nome": "BBDC4", "valor": 10},
         "ABEV3": {"nome": "ABEV3", "valor": 10}, "PETR3": {"nome": "PETR3", "valor": 10},
         "LREN3": {"nome": "LREN3", "valor": 10}, "ITSA3": {"nome": "ITSA3", "valor": 10},
         "JBSS3": {"nome": "JBSS3", "valor": 10}, "RAIL3": {"nome": "RAIL3", "valor": 10},
         "MGLU3": {"nome": "MGLU3", "valor": 10}, "KROT3": {"nome": "KROT3", "valor": 10},
         "NATU3": {"nome": "NATU3", "valor": 10}, "CIEL3": {"nome": "CIEL3", "valor": 10},
         "SUZB3": {"nome": "SUZB3", "valor": 10}, "UGPA3": {"nome": "UFPA3", "valor": 10},
         "GOLL4": {"nome": "GOLL4", "valor": 10}, "SMLS3": {"nome": "SMLS3", "valor": 10}}

def variacao(acao):
    acao["valor"] += random.uniform(-5,5)

def main():
    """main method"""

    # Prepare our context and publisher
    context   = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://*:5563")

    while True:
        # Write two messages, each with an envelope and content
        for acao in acoes:
            acoes[acao]["valor"] += random.uniform(-10, 10)
            if(acoes[acao]["valor"] < 0):
                acoes[acao]["valor"] = 10
            valor = bytes(str(round(acoes[acao]["valor"], 2)),'utf-8')
            publisher.send_multipart([bytes(acao, 'utf-8'), valor])
        time.sleep(1)

    # We never get here but clean up anyhow
    publisher.close()
    context.term()

if __name__ == "__main__":
    main()