import csv


class IP2CountryMap(object):
    ip_map = None
    ip_ranges = None

    @classmethod
    def _set_ip_country_map(cls):
        with open('IpToCountry.csv', 'r') as f:
            csv_file = csv.reader(f)
            cls.ip_map = {}
            cls.ip_ranges = []
            for x in csv_file:
                if x[0][0] != '#':
                    map_key = (int(x[0]), int(x[1]))
                    cls.ip_map[map_key] = x[6]
                    cls.ip_ranges.append(map_key)

    def search(self, ip_addr):
        self._validate(ip_addr)
        ip_identifier = self._calculate_id(ip_addr)
        for ip_range in self.ip_ranges:
            if ip_identifier >= ip_range[0] and ip_identifier <= ip_range[1]:
                return self.ip_map[ip_range]

    def _calculate_id(self, ip_addr):
        multiplier = 1
        result = 0
        ip_addr = ip_addr.split('.')
        ip_addr.reverse()
        for section in ip_addr:
            result += int(section) * multiplier
            multiplier *= 256
        return result

    def _validate(self, ip_addr):
        try:
            for section in ip_addr.split('.'):
                section = int(section)
                if section > 255:
                    raise Exception('Invalid ip')
        except:
            raise Exception('Invalid ip')

IP2CountryMap._set_ip_country_map()

if __name__ == '__main__':
    ip_addr = raw_input('IP -> ')
    print IP2CountryMap().search(ip_addr)
