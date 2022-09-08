class Flight:
    def __init__(self, engine):
        self.engine = engine

    def startEngine(self):
        self.engine.start()

class AirbusEngine:
    def start(self):
        print("Starting Airbus Engine")

class BoingEngine:
    def start(self):
        print("Starting Boing Engine")

airbusEngine = AirbusEngine()
boingEngine = BoingEngine()

flight = Flight(airbusEngine)
flight.startEngine()

flight2 = Flight(boingEngine)
flight2.startEngine()