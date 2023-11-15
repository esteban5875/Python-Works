import random

class Codes:
    def __init__(self):
        self.codes_generated = set()
    @staticmethod
    def generate_code():
        while True:
            result_code = random.randint(10000000000, 99999999999)
            if result_code not in Codes.codes_generated:
                Codes.codes_generated.add(result_code)
                break