import random
import time
import zmq

# processos para o cálculo da ação e publicação
def petr4(acoes, publisher,lock):
    while True:
        acoes["PETR4"]["valor"] += random.uniform(-10, 10)
        if acoes["PETR4"]["valor"] < 0:
            acoes["PETR4"]["valor"] = 10
        valor = bytes(str(round(acoes["PETR4"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["PETR4"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def vale3(acoes, publisher,lock):
    while True:
        acoes["VALE3"]["valor"] += random.uniform(-10, 10)
        if acoes["VALE3"]["valor"] < 0:
            acoes["VALE3"]["valor"] = 10
        valor = bytes(str(round(acoes["VALE3"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["VALE3"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def itub4(acoes, publisher,lock):
    while True:
        acoes["ITUB4"]["valor"] += random.uniform(-10, 10)
        if acoes["ITUB4"]["valor"] < 0:
            acoes["ITUB4"]["valor"] = 10
        valor = bytes(str(round(acoes["ITUB4"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["ITUB4"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def b3sa3(acoes, publisher,lock):
    while True:
        acoes["B3SA3"]["valor"] += random.uniform(-10, 10)
        if acoes["B3SA3"]["valor"] < 0:
            acoes["B3SA3"]["valor"] = 10
        valor = bytes(str(round(acoes["B3SA3"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["B3SA3"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def bbas3(acoes, publisher,lock):
    while True:
        acoes["BBAS3"]["valor"] += random.uniform(-10, 10)
        if acoes["BBAS3"]["valor"] < 0:
            acoes["BBAS3"]["valor"] = 10
        valor = bytes(str(round(acoes["BBAS3"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["BBAS3"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def bbdc4(acoes, publisher,lock):
    while True:
        acoes["BBDC4"]["valor"] += random.uniform(-10, 10)
        if acoes["BBDC4"]["valor"] < 0:
            acoes["BBDC4"]["valor"] = 10
        valor = bytes(str(round(acoes["BBDC4"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["BBDC4"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def abev3(acoes, publisher,lock):
    while True:
        acoes["ABEV3"]["valor"] += random.uniform(-10, 10)
        if acoes["ABEV3"]["valor"] < 0:
            acoes["ABEV3"]["valor"] = 10
        valor = bytes(str(round(acoes["ABEV3"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["ABEV3"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def petr3(acoes, publisher,lock):
    while True:
        acoes["PETR3"]["valor"] += random.uniform(-10, 10)
        if acoes["PETR3"]["valor"] < 0:
            acoes["PETR3"]["valor"] = 10
        valor = bytes(str(round(acoes["PETR3"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["PETR3"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def lren3(acoes, publisher,lock):
    while True:
        acoes["LREN3"]["valor"] += random.uniform(-10, 10)
        if acoes["LREN3"]["valor"] < 0:
            acoes["LREN3"]["valor"] = 10
        valor = bytes(str(round(acoes["LREN3"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["LREN3"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def itsa3(acoes, publisher,lock):
    while True:
        acoes["ITSA3"]["valor"] += random.uniform(-10, 10)
        if acoes["ITSA3"]["valor"] < 0:
            acoes["ITSA3"]["valor"] = 10
        valor = bytes(str(round(acoes["ITSA3"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["ITSA3"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def jbss3(acoes, publisher,lock):
    while True:
        acoes["JBSS3"]["valor"] += random.uniform(-10, 10)
        if acoes["JBSS3"]["valor"] < 0:
            acoes["JBSS3"]["valor"] = 10
        valor = bytes(str(round(acoes["JBSS3"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["JBSS3"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def rail3(acoes, publisher,lock):
    while True:
        acoes["RAIL3"]["valor"] += random.uniform(-10, 10)
        if acoes["RAIL3"]["valor"] < 0:
            acoes["RAIL3"]["valor"] = 10
        valor = bytes(str(round(acoes["RAIL3"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["RAIL3"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def mglu3(acoes, publisher,lock):
    while True:
        acoes["MGLU3"]["valor"] += random.uniform(-10, 10)
        if acoes["MGLU3"]["valor"] < 0:
            acoes["MGLU3"]["valor"] = 10
        valor = bytes(str(round(acoes["MGLU3"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["MGLU3"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def krot3(acoes, publisher,lock):
    while True:
        acoes["KROT3"]["valor"] += random.uniform(-10, 10)
        if acoes["KROT3"]["valor"] < 0:
            acoes["KROT3"]["valor"] = 10
        valor = bytes(str(round(acoes["KROT3"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["KROT3"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def natu3(acoes, publisher,lock):
    while True:
        acoes["NATU3"]["valor"] += random.uniform(-10, 10)
        if acoes["NATU3"]["valor"] < 0:
            acoes["NATU3"]["valor"] = 10
        valor = bytes(str(round(acoes["NATU3"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["NATU3"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def ciel3(acoes, publisher,lock):
    while True:
        acoes["CIEL3"]["valor"] += random.uniform(-10, 10)
        if acoes["CIEL3"]["valor"] < 0:
            acoes["CIEL3"]["valor"] = 10
        valor = bytes(str(round(acoes["CIEL3"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["CIEL3"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def suzb3(acoes, publisher,lock):
    while True:
        acoes["SUZB3"]["valor"] += random.uniform(-10, 10)
        if acoes["SUZB3"]["valor"] < 0:
            acoes["SUZB3"]["valor"] = 10
        valor = bytes(str(round(acoes["SUZB3"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["SUZB3"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def ugpa3(acoes, publisher,lock):
    while True:
        acoes["UGPA3"]["valor"] += random.uniform(-10, 10)
        if acoes["UGPA3"]["valor"] < 0:
            acoes["UGPA3"]["valor"] = 10
        valor = bytes(str(round(acoes["UGPA3"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["UGPA3"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def goll4(acoes, publisher,lock):
    while True:
        acoes["GOLL4"]["valor"] += random.uniform(-10, 10)
        if acoes["GOLL4"]["valor"] < 0:
            acoes["GOLL4"]["valor"] = 10
        valor = bytes(str(round(acoes["GOLL4"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["GOLL4"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

def smls3(acoes, publisher,lock):
    while True:
        acoes["SMLS3"]["valor"] += random.uniform(-10, 10)
        if acoes["SMLS3"]["valor"] < 0:
            acoes["SMLS3"]["valor"] = 10
        valor = bytes(str(round(acoes["SMLS3"]["valor"], 2)), 'utf-8')
        lock.acquire()
        publisher.send_multipart([bytes(acoes["SMLS3"]["nome"], 'utf-8'), valor])
        lock.release()
        time.sleep(1)

