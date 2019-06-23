import zmq

def main():
    """ main method """

    # Prepare our context and publisher
    context    = zmq.Context()
    subscriber = context.socket(zmq.SUB)
    subscriber.connect("tcp://localhost:5563")
    subscriber.setsockopt(zmq.SUBSCRIBE, b'CIEL3')

    while True:
        # Read envelope with address
        acao, valor = subscriber.recv_multipart()
        print("%s Valor: R$ %s" % (acao.decode('utf-8'), valor.decode('utf-8')))

    # We never get here but clean up anyhow
    subscriber.close()
    context.term()

if __name__ == "__main__":
    main()