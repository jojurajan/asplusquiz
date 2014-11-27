import unittest
from subprocess import check_output
from country_ip import CountryIp


class CountryIpTest(unittest.TestCase):
    def setUp(self):
        self.country_ip = CountryIp()

    def test_bad_input_raises_exception(self):
        with self.assertRaises(Exception) as cm:
            self.country_ip.search("Foo")

        self.assertEqual(cm.exception.message, 'Invalid ip')

    def test_invalid_ip_raises_exception(self):
        invalid_ips = ['300.10.10.10', '10.300.10.10', '10.10.300.10', '10.10.10.300']
        for invalid_ip in invalid_ips:
            with self.assertRaises(Exception) as cm:
                self.country_ip.search(invalid_ip)

            self.assertEqual(cm.exception.message, 'Invalid ip')

    def test_csv_file_not_changed(self):
        # For Ubuntu machines
        self.assertEqual(check_output(['md5sum', 'IpToCountry.csv']).split(' ')[0], '22620fdd50ebaef84dd3d9521beb6a7c')

    def test_67_99_163_76_is_United_States(self):
        self.assertEqual("United States", self.country_ip.search("67.99.163.76"))

    def test_10_12_14_19_is_Reserved(self):
        self.assertEqual("Reserved", self.country_ip.search("10.12.14.19"))

    def test_200_100_100_100_is_Brazil(self):
        self.assertEqual("Brazil", self.country_ip.search("200.100.100.100"))


if __name__ == '__main__':
    unittest.main()
