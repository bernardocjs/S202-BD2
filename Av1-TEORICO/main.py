from database import Database
import random
import threading
import time

trigger = 38
dbDatabase = "bancoiot"
dbCollection = "sensores"
db = Database()
collection = db.connect(dbDatabase, dbCollection)


def createSensor():
    collection.insert_one({
        "nomeSensor": "sensor1",
        "valorSensor": 0,
        "unidadeMedida": "°C",
        "sensorAlarmadado": False
    })
    collection.insert_one({
        "nomeSensor": "sensor2",
        "valorSensor": 0,
        "unidadeMedida": "°C",
        "sensorAlarmadado": False
    })
    collection.insert_one({
        "nomeSensor": "sensor3",
        "valorSensor": 0,
        "unidadeMedida": "°C",
        "sensorAlarmadado": False
    })


def sensorVariation(sensorName, sleepTime):
    try:
        while True:
            sensorValue = random.uniform(30, 40)
            if (sensorValue > trigger):
                sensorAlarmado = True
            else:
                sensorAlarmado = False

            replaceDocs = {
                "valorSensor": sensorValue,
                "sensorAlarmadado": sensorAlarmado
            }

            print(f"sensor {sensorName}: {sensorValue}°C")
            collection.update_one({"nomeSensor": sensorName},
                                  {"$set": replaceDocs})

            if (sensorAlarmado):
                raise Exception(
                    f'Atenção! Temperatura muito alta! Verificar o Sensor {sensorName}'
                )
            time.sleep(sleepTime)

    except Exception as e:
        print(e)
        exit()


createSensor()
x1 = threading.Thread(target=sensorVariation, args=("sensor1", 3))
x1.start()
x2 = threading.Thread(target=sensorVariation, args=("sensor2", 3))
x2.start()
x3 = threading.Thread(target=sensorVariation, args=("sensor3", 3))
x3.start()
