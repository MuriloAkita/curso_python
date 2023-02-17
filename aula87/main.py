from calculadora_ipv4 import IPv4Calculator

ip = IPv4Calculator(ip='10.20.12.45', prefix=26)

print(f'IP: {ip.ip}')
print(f'Máscara: {ip.mask}')
print(f'Rede: {ip.network}')
print(f'Broadcast: {ip.broadcast}')
print(f'Prefixo: {ip.prefix}')
print(f'Número de IPs da rede: {ip.max_ip}')


