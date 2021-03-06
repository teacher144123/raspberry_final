import RPi.GPIO as gpio
import json, time, random
from threading import Thread

from register import Register

class Matrix:
    def __init__(self, num_layer=20, online=False):
        self.now_layer = 0
        self.max_layer = num_layer

        self.maps, self.graph = self.makeGraph(num_layer)

    def startPrint(self, step=2, width=8, delay=1):
        self.th = Thread(target=self._startPrint, args=(step, width, delay,))
        self.th.start()
        # th.join()

    def _startPrint(self, step, width, delay):
        self.register = Register(self.DS, self.SHCP, self.STCP)
        while self.now_layer < self.max_layer:
            i = self.now_layer * 2
            graph_slice = self.graph[i : i + width]

            # print to 8x8
            self.show8x8(graph_slice, sec=delay)

    def makeGraph(self, num_layer):
        with open('data/layer.json') as json_f:
            data = json.loads(json_f.read())

        maps = []
        graph = []
        for i in range(num_layer):
            r_int = random.randint(1, 10)
            if r_int <= 7:
                sub_data = data['one_layer']
            else:
                sub_data = data['two_layer']

            keys = list(sub_data.keys())
            r_int = random.randint(0, len(keys) - 1)

            maps.append(keys[r_int])
            graph += sub_data[keys[r_int]]


        # to think
        graph += ["00000000"] * 8

        return maps, graph

def makeWords(words):
    with open('data/hello.json') as json_f:
        data = json.loads(json_f.read())

    graph = []
    for w in words:
        graph += data[w]

    return graph

if __name__ == '__main__':
    try:
        matrix = LEDMatrix()

        matrix.graph = makeWords('hello')

        matrix.startPrint(delay=0.5)

        time.sleep(100)
    finally:
        gpio.cleanup()
