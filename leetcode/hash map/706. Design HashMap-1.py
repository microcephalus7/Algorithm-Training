# dictionary 로 만들기

class MyHashMap:

    def __init__(self):
        self.hash_map = {}

    def put(self, key: int, value: int) -> None:
        self.hash_map[key] = value

    def get(self, key: int) -> int:
        if key in self.hash_map:
            return self.hash_map[key]
        else:
            return -1

    def remove(self, key: int) -> None:
        if key in self.hash_map:
            del self.hash_map[key]
