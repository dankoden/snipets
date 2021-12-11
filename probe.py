import queue
import random
from collections import defaultdict
from multiprocessing import Process ,Pipe, Queue
from queue import Empty
import threading

FISH = [None, "Окунь","Карась","Щука","Лосось"]
NAME = ["Петя", "Степя","Вася","Хмурый","Игорь"]


class Fishers(threading.Thread):

    def __init__(self,name ,worms,catcher,*args,**kwargs):
        super(Fishers, self).__init__(*args,**kwargs)
        self.name = name
        self.worms = worms
        self.catcher = catcher

    def run(self):
        for worm in range(self.worms):
            print(f"{self.name}: закинул червяка {worm}....Ждем",flush=True)
            _ = 3 * 10**1313
            fish = random.choice(FISH)
            if fish is None:
                print(f"{self.name}: Черт сорвалась рыба",flush=True)
            else:
                print(f"{self.name}: Ага поймал {fish} и хочет положить его в сачок",flush=True)
                if self.catcher.full():
                    print(f"{self.name}{worm}: приемщик полон",flush=True)
                self.catcher.put(fish)
                print(f"{self.name}{worm}: положил рыбу {fish} в приемщик", flush=True)

class Boat(threading.Thread):

    def __init__(self,worms_for_fisher):
        super(Boat, self).__init__()
        self.fishers = []
        self.worms_for_fishers = worms_for_fisher
        self.catcher = queue.Queue(maxsize=2)
        self.fish_tank = defaultdict(int)

    def add_fisher(self,name):
        fisher = Fishers(worms=10, name=name,catcher=self.catcher)
        self.fishers.append(fisher)

    def run(self):
        print("Лодка вышла в море",flush=True)
        for fisher in self.fishers:
            fisher.start()
        while True:
            try:
                fish = self.catcher.get(timeout=1)
                print(f'Приемщик принял {fish} и положил в сачок', flush=True)
                self.fish_tank[fish] +=1

            except queue.Empty:
                print(f'Приемщику нет рыбы в течении 1 секунды', flush=True)
                if not any(fisher.is_alive() for fisher in self.fishers):
                    break
        for fisher in self.fishers:
            fisher.join()
        print(f'Лодка возвращается домой с {self.fish_tank}', flush=True)

boat = Boat(worms_for_fisher=10)
for name in NAME:
    boat.add_fisher(name=name)

boat.start()
boat.join()

print(f'Лодка привезла домой с {boat.fish_tank}', flush=True)








