class IPv4Calculator:

    def __init__(self, ip: str, prefix: int):
        self.ip = ip
        self.prefix = prefix
        self._set_mask()
        self._set_max_ip()
        self._set_network()
        self._set_broadcast()

    @property
    def ip(self):
        return self._ip

    @ip.setter
    def ip(self, valor):
        if not self._ip_validation(valor):
            raise ValueError('IP Inválido.')
        self._ip = valor

    @property
    def prefix(self):
        return self._prefix

    @prefix.setter
    def prefix(self, valor):
        if not isinstance(valor, int):
            raise TypeError('O prefixo precisa ser um número inteiro.')

        if valor > 32:
            raise ValueError('O prefixo não pode ser acima de 32 Bits.')

        self._prefix = valor

    @property
    def mask(self):
        return self._mask

    @property
    def max_ip(self):
        return self._max_ip

    @property
    def network(self):
        return self._network

    @property
    def broadcast(self):
        return self._broadcast

    @staticmethod
    def _ip_validation(ip: str):

        if not ip.__contains__('.'):
            return False

        try:
            ip_array = ip.split('.')
            ip_array = list(map(int, ip_array))

            for n in ip_array:
                if n > 255:
                    return False

            return True
        except ValueError:
            return False

    @staticmethod
    def ip_to_bin(ip):
        ip_list = ip.split('.')
        ip_bin_list = [str(bin(int(n))[2:].zfill(8)) for n in ip_list]
        return ip_bin_list

    @staticmethod
    def bin_to_ip(ip_bin_list):
        ip = [str(int(n, 2)) for n in ip_bin_list]
        return ip

    def _set_mask(self):
        mask_bin = (self.prefix * '1').ljust(32, '0')
        mask_list = [str(int(mask_bin[i:i + 8], 2)) for i in range(0, len(mask_bin), 8)]

        self._mask = '.'.join(mask_list)

    def _set_max_ip(self):
        self._max_ip = 2 ** (32 - self._prefix)

    def _set_network(self):
        port = 32 - self._prefix

        if port >= 8:
            port = 8

        ip_bin = self.ip_to_bin(self.ip)
        ip_bin[3] = ip_bin[3][:8 - port].ljust(8, '0')
        ip_list = self.bin_to_ip(ip_bin)

        self._network = '.'.join(ip_list)

    def _set_broadcast(self):
        port = 32 - self._prefix

        if port >= 8:
            port = 8

        ip_bin = self.ip_to_bin(self.ip)
        ip_bin[3] = ip_bin[3][:8 - port].ljust(8, '1')
        ip_list = self.bin_to_ip(ip_bin)

        self._broadcast = '.'.join(ip_list)
