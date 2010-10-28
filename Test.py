import unittest
import Seconds

class testSeconds(unittest.TestCase):
    def testFull(self):
        string = '%D day(s) %H hour(s) %M minute(s) %S second(s)'
        self.assertEqual(Seconds.Seconds(0, string), '')
        self.assertEqual(Seconds.Seconds(67, string), '1 minute 7 seconds')
        self.assertEqual(Seconds.Seconds(256, string), '4 minutes 16 seconds')
        self.assertEqual(Seconds.Seconds(3720, string), '1 hour 2 minutes')
        self.assertEqual(Seconds.Seconds(11046, string), '3 hours 4 minutes 6 seconds')        
        self.assertEqual(Seconds.Seconds(2687692, string), '31 days 2 hours 34 minutes 52 seconds')

    def testStamp(self):
        string = '%D:%H:%M:%S'
        self.assertEqual(Seconds.Seconds(0, string), '')
        self.assertEqual(Seconds.Seconds(67, string), '1:7')
        self.assertEqual(Seconds.Seconds(256, string), '4:16')
        self.assertEqual(Seconds.Seconds(3720, string, True), '0:1:2:0')
        self.assertEqual(Seconds.Seconds(11046, string), '3:4:6')       
        self.assertEqual(Seconds.Seconds(2687692, string), '31:2:34:52')

    def testShort(self):
        string = '%Dd %Hh %Mm %Ss'
        self.assertEqual(Seconds.Seconds(0, string), '')
        self.assertEqual(Seconds.Seconds(67, string), '1m 7s')
        self.assertEqual(Seconds.Seconds(256, string), '4m 16s')
        self.assertEqual(Seconds.Seconds(3720, string), '1h 2m')
        self.assertEqual(Seconds.Seconds(11046, string), '3h 4m 6s')        
        self.assertEqual(Seconds.Seconds(2687692, string), '31d 2h 34m 52s')
        
    def testCarryOver(self):  
        self.assertEqual(Seconds.Seconds(67, '%Ss'), '67s') 
        self.assertEqual(Seconds.Seconds(5000, '%Mm %Ss'), '83m 20s')
        self.assertEqual(Seconds.Seconds(7321, '%M minute(s) %S second(s)'), '122 minutes 1 second')
        
    def testZero(self):
        string = '%D day %H hr %M min %S sec'
        self.assertEqual(Seconds.Seconds(0, string, True), '0 day 0 hr 0 min 0 sec') 
        self.assertEqual(Seconds.Seconds(3600, string, True), '0 day 1 hr 0 min 0 sec')   
        
        string = '%D day(s) %H hour(s) %M minute(s) %S second(s)'
        self.assertEqual(Seconds.Seconds(0, string, True), '0 days 0 hours 0 minutes 0 seconds')
        self.assertEqual(Seconds.Seconds(3600, string, True), '0 days 1 hour 0 minutes 0 seconds')
        self.assertEqual(Seconds.Seconds(3662, string, True), '0 days 1 hour 1 minute 2 seconds')      

if __name__ == '__main__':
    unittest.main()
