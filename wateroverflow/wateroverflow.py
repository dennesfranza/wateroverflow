import argparse

class Glass(object):

    def __init__(self, fill=0):
        self.capacity = 250
        self.fill = fill

    def __repr__(self):
        if self.is_full():
            return '{0:^4}'.format('|▇|')
        elif self.fill >= self.capacity / 2:
            return '{0:^4}'.format('|▅|')
        elif self.fill > 0 and self.fill < self.capacity / 2:
            return '{0:^4}'.format('|▂|')
        else:
            return '{0:4}'.format('|_|')

    def is_full(self):
        if self.fill >= self.capacity:
            return True
        return False

    def overflow(self):
        return self.fill - self.capacity

class WaterOverflow(object):

    def __init__(self, liters):
        self.liters = int(liters * 1000)
        self.glasses = []

    def populate(self):
        glasses = [[Glass()]]
        glasses[0][0].fill = self.liters
        row = 1

        flowing = True
        while flowing:
            flowing = False
            nrow = False
            for _glass in range(row):
                _row = row - 1
                if glasses[_row][_glass].is_full():
                    if nrow == False:
                        next_row = [Glass() for _ in range(row + 1)]
                        glasses.append(next_row)
                        nrow = True
                    overflow = glasses[_row][_glass].overflow()
                    glasses[_row][_glass].fill = 250
                    glasses[_row + 1][_glass].fill += overflow / 2
                    glasses[_row + 1][_glass + 1].fill += overflow / 2
                    flowing = True
            row += 1
        self.glasses = glasses

    def illustrate(self):
        self.populate()
        row = len(self.glasses) - 1
        for _row in self.glasses:
            row_glasses = []
            for glass in _row:
                row_glasses.append(str(glass))
            print('{0:2}'.format(' ') * row, ''.join(row_glasses))
            row -= 1

def is_float(i):
    try:
        a = float(i)
    except (TypeError, ValueError):
        return False
    else:
        return True

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-l', '--liters', dest='liters', required=True)

    results = parser.parse_args()

    if is_float(results.liters):
        wateroverflow = WaterOverflow(float(results.liters))
        wateroverflow.illustrate()


if __name__ == '__main__':
    main()
