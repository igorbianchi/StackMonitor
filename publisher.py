import zmq
import threading
import processos as proc

# definição das ações disponíveis e valores iniciais
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


def main():
    # prepara o contexto e o publicador
    context   = zmq.Context()
    publisher = context.socket(zmq.PUB)
    publisher.bind("tcp://*:5563")

    # cria um objeto para travar a exeucação dos processos quando for fazer uma publicação
    lock = threading.Lock()

    # cria os processos paralelos
    petr4 = threading.Thread(target=proc.petr4, args=(acoes, publisher, lock))
    vale3 = threading.Thread(target=proc.vale3, args=(acoes, publisher, lock))
    itub4 = threading.Thread(target=proc.itub4, args=(acoes, publisher, lock))
    b3sa3 = threading.Thread(target=proc.b3sa3, args=(acoes, publisher, lock))
    abev3 = threading.Thread(target=proc.abev3, args=(acoes, publisher, lock))
    bbdc4 = threading.Thread(target=proc.bbdc4, args=(acoes, publisher, lock))
    petr3 = threading.Thread(target=proc.petr3, args=(acoes, publisher, lock))
    lren3 = threading.Thread(target=proc.lren3, args=(acoes, publisher, lock))
    itsa3 = threading.Thread(target=proc.itsa3, args=(acoes, publisher, lock))
    jbss3 = threading.Thread(target=proc.jbss3, args=(acoes, publisher, lock))
    rail3 = threading.Thread(target=proc.rail3, args=(acoes, publisher, lock))
    mglu3 = threading.Thread(target=proc.mglu3, args=(acoes, publisher, lock))
    krot3 = threading.Thread(target=proc.krot3, args=(acoes, publisher, lock))
    natu3 = threading.Thread(target=proc.natu3, args=(acoes, publisher, lock))
    ciel3 = threading.Thread(target=proc.ciel3, args=(acoes, publisher, lock))
    suzb3 = threading.Thread(target=proc.suzb3, args=(acoes, publisher, lock))
    ugpa3 = threading.Thread(target=proc.ugpa3, args=(acoes, publisher, lock))
    goll4 = threading.Thread(target=proc.goll4, args=(acoes, publisher, lock))
    smls3 = threading.Thread(target=proc.smls3, args=(acoes, publisher, lock))


    vale3.start()
    petr4.start()
    itub4.start()
    b3sa3.start()
    bbdc4.start()
    abev3.start()
    petr3.start()
    lren3.start()
    itsa3.start()
    jbss3.start()
    rail3.start()
    mglu3.start()
    krot3.start()
    natu3.start()
    ciel3.start()
    suzb3.start()
    ugpa3.start()
    goll4.start()
    smls3.start()



if __name__ == "__main__":
    main()