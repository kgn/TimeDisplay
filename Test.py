import unittest
import Runtime

class testRuntime(unittest.TestCase):
    def test0seconds(self):
        self.assertEqual(Runtime.Runtime(0), '')

    def testSecond(self):
        self.assertEqual(Runtime.Runtime(1), '1 second')
        self.assertEqual(Runtime.Runtime(1, second='sec'), '1 sec')
        self.assertEqual(Runtime.Runtime(1, second='s'), '1 s')

    def testSeconds(self):
        self.assertEqual(Runtime.Runtime(35), '35 seconds')
        self.assertEqual(Runtime.Runtime(27, second='s', pluralize=False), '27 s')
        self.assertEqual(Runtime.Runtime(45, second='sec', pluralize=False), '45 sec')

    def testMinute(self):
        self.assertEqual(Runtime.Runtime(60), '1 minute')
        self.assertEqual(Runtime.Runtime(60, minute='min'), '1 min')
        self.assertEqual(Runtime.Runtime(60, minute='m'), '1 m')

    def testMinuteSeconds(self):
        self.assertEqual(Runtime.Runtime(61), '1 minute 1 second')
        self.assertEqual(Runtime.Runtime(67), '1 minute 7 seconds')
        self.assertEqual(Runtime.Runtime(65, second='sec', minute='min', pluralize=False), '1 min 5 sec')
        self.assertEqual(Runtime.Runtime(63, second='s', minute='m', pluralize=False), '1 m 3 s')
        self.assertEqual(Runtime.Runtime(96), '1 minute 36 seconds')

    def testJustMinutes(self):
        self.assertEqual(Runtime.Runtime(120), '2 minutes')
        self.assertEqual(Runtime.Runtime(240, minute='min', pluralize=False), '4 min')
        self.assertEqual(Runtime.Runtime(300, minute='m', pluralize=False), '5 m')
        self.assertEqual(Runtime.Runtime(1620), '27 minutes')

    def testMinutesSeconds(self):
        self.assertEqual(Runtime.Runtime(256), '4 minutes 16 seconds')
        self.assertEqual(Runtime.Runtime(1028, minute='min'), '17 mins 8 seconds')
        self.assertEqual(Runtime.Runtime(2050, minute='m', second='s', pluralize=False), '34 m 10 s')

    def testHour(self):
        self.assertEqual(Runtime.Runtime(3600), '1 hour')
        self.assertEqual(Runtime.Runtime(3600, hour='h'), '1 h')
        self.assertEqual(Runtime.Runtime(3600, hour='hr'), '1 hr')

    def testHours(self):
        self.assertEqual(Runtime.Runtime(7200), '2 hours')
        self.assertEqual(Runtime.Runtime(14400, hour='h'), '4 hs')
        self.assertEqual(Runtime.Runtime(18000, hour='hr', pluralize=False), '5 hr')

    def testHourMinute(self):
        self.assertEqual(Runtime.Runtime(3660), '1 hour 1 minute')
        self.assertEqual(Runtime.Runtime(3660, hour='hr', minute='min'), '1 hr 1 min')

    def testHoursMinute(self):
        self.assertEqual(Runtime.Runtime(3720), '1 hour 2 minutes')
        self.assertEqual(Runtime.Runtime(5220), '1 hour 27 minutes')
        self.assertEqual(Runtime.Runtime(5220, minute='min', hour='hr'), '1 hr 27 mins')

    def testHoursMinutes(self):
        self.assertEqual(Runtime.Runtime(7920), '2 hours 12 minutes')
        self.assertEqual(Runtime.Runtime(17100, minute='min', hour='hr', pluralize=False), '4 hr 45 min')
        self.assertEqual(Runtime.Runtime(43800, minute='m', hour='h', pluralize=False), '12 h 10 m')

    def testHourMinuteSecond(self):
        self.assertEqual(Runtime.Runtime(3661), '1 hour 1 minute 1 second')
        self.assertEqual(Runtime.Runtime(3661, hour='h', minute='m', second='s'), '1 h 1 m 1 s')
        self.assertEqual(Runtime.Runtime(3661, hour='hr', minute='min', second='sec'), '1 hr 1 min 1 sec')

    def testHoursMinuteSecond(self):
        self.assertEqual(Runtime.Runtime(21661), '6 hours 1 minute 1 second')
        self.assertEqual(Runtime.Runtime(43261, second='sec'), '12 hours 1 minute 1 sec')

    def testHoursMinutesSecond(self):
        self.assertEqual(Runtime.Runtime(11041), '3 hours 4 minutes 1 second')
        self.assertEqual(Runtime.Runtime(7381, second='sec', minute='min'), '2 hours 3 mins 1 sec')

    def testHoursMinutesSeconds(self):
        self.assertEqual(Runtime.Runtime(11046), '3 hours 4 minutes 6 seconds')
        self.assertEqual(Runtime.Runtime(21724, hour='hr', second='sec'), '6 hrs 2 minutes 4 secs')

    def testDay(self):
        self.assertEqual(Runtime.Runtime(86400), '1 day')
        self.assertEqual(Runtime.Runtime(86400, day='d'), '1 d')

    def testDays(self):
        self.assertEqual(Runtime.Runtime(259200), '3 days')
        self.assertEqual(Runtime.Runtime(1728000, day='d', pluralize=False), '20 d')

    def testDaysHoursMinutesSeconds(self):
        self.assertEqual(Runtime.Runtime(2687692), '31 days 2 hours 34 minutes 52 seconds')

    def test0hours(self):
        self.assertEqual(Runtime.Runtime(2680492), '31 days 34 minutes 52 seconds')

if __name__ == '__main__':
    unittest.main()
