import unittest

from wateroverflow.wateroverflow import *

class TestOverFlow(unittest.TestCase):

	def test_wateroverflow(self):
		wateroverflow = WaterOverflow(4.0)
		wateroverflow.populate()
		self.assertEqual(wateroverflow.glasses[1][1].fill, 250)
		self.assertEqual(wateroverflow.glasses[2][2].fill, 250)
		self.assertEqual(wateroverflow.glasses[4][0].fill, 15.625)
		self.assertEqual(wateroverflow.glasses[5][0].fill, 0)
		self.assertEqual(wateroverflow.glasses[6][2].fill, 23.4375)

	def test_liters(self):
		liters = []
		wateroverflow = WaterOverflow(5.1)
		wateroverflow.populate()
		for _ir, row in enumerate(wateroverflow.glasses):
			for _ig, glass in enumerate(row):
				liters.append(glass.fill)
		sum_liters = sum(liters) / 1000
		self.assertEqual(sum_liters, 5.1)

	def test_glass(self):
		self.assertFalse(Glass(200).is_full())


if __name__ == '__main__':
	unittest.main()
