import csv


class CountryIp(object):
    '''
    Find the country to which the given IP is allocated
    '''
    ip_map = None
    ip_ranges = None

    def __init__(self):
        self._set_ip_country_map()

    def _set_ip_country_map(self):
        '''
        * Load data from IpToCountry.csv into a mapping of the following structure:
            ip_identifier_range: country_name
        * Set the ip_identifier_range values into a list for each access
        '''
        with open('IpToCountry.csv', 'r') as f:
            csv_file = csv.reader(f)
            self.ip_map = {}
            self.ip_ranges = []
            for x in csv_file:
                if x[0][0] != '#':
                    map_key = (int(x[0]), int(x[1]))
                    self.ip_map[map_key] = x[6]
                    self.ip_ranges.append(map_key)

    def search(self, ip_addr):
        '''
        Search for the country which matches the specified ip address.
            * The ip address is validated.
            * The ip_identifier is calculated to check in the generated ip mapping
            * The ip_identifier is checked against the mapping.
                - If match is found, it returns country name
                - Else, returns None
        '''
        self._validate(ip_addr)
        ip_identifier = self._calculate_id(ip_addr)
        for ip_range in self.ip_ranges:
            if ip_identifier >= ip_range[0] and ip_identifier <= ip_range[1]:
                return self.ip_map[ip_range]

    def _calculate_id(self, ip_addr):
        '''
        Calculates the identifier for the passed ip address.
            * The ip is split into sections, for each octet
            * The identifier is calculated as follows:
                - e.g. for 1.2.3.4, identifier would be calculated as
                    1*(256*256*256) + 2*(256*256) + 3*(256) + 4*(1)
        '''
        multiplier = 1
        result = 0
        ip_addr = ip_addr.split('.')
        ip_addr.reverse()
        for section in ip_addr:
            result += int(section) * multiplier
            multiplier *= 256
        return result

    def _validate(self, ip_addr):
        '''
        Validates the passed ip address string.
            * Checks by typecasting each octet section into int
            * Checks for each section to be greater than -1 and less than 255
        '''
        try:
            for section in ip_addr.split('.'):
                section = int(section)
                if section < 0 or section > 255:
                    raise Exception('Invalid ip')
        except:
            raise Exception('Invalid ip')


if __name__ == '__main__':
    ip_addr = raw_input('IP -> ')
    print CountryIp().search(ip_addr)
