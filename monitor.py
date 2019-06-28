import zmq
import time
import datetime

def main():

    # prepara o contexto e o assinante
    context    = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://localhost:5563")
    # assina todas as ações
    subscriber.setsockopt(zmq.SUBSCRIBE, b'')

    while True:
        hora = datetime.datetime.now()
        try:
            # recebe os dados de assinante
            acao, valor = subscriber.recv_multipart()
            print("%s Valor: R$ %s às %d:%d:%d" % (acao.decode('utf-8'), valor.decode('utf-8'), hora.hour, hora.minute, hora.second))
            time.sleep(0.1)
        except:
           time.sleep(5)


    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()