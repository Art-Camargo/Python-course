import re


def muda_arquivo(URL,ips_validos, ips_invalidos):
    with open(URL, 'r+') as arquivo_novo:
        arquivo_novo.writelines(f'[Ips Válidos abaixo]\n\n')
        for ips_v in ips_validos:
            arquivo_novo.writelines(f'{ips_v}\n')
        arquivo_novo.writelines(f'\n\n\n[Ips Inválidos abaixo]\n\n')
        for ips_i in ips_invalidos:
            arquivo_novo.writelines(f'{ips_i}\n')

def main():
    URL = 'ips.txt'
    with open(URL, 'r') as arquivo:
        ips_lista = list(arquivo.readlines())
        ips_lista = [ips.strip() for ips in ips_lista]
    ips_regex = re.compile(r'^(?:2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(?:2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(?:2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])\.(?:2[0-5][0-5]|1[0-9][0-9]|[1-9][0-9]|[0-9])$')

    ips_validos = []
    ips_invalidos = []
    for ip in ips_lista:
        if ips_regex.search(ip):
            ips_validos.append(ip)
        else:
            ips_invalidos.append(ip)
    muda_arquivo(URL, ips_validos, ips_invalidos)
    print(f'O arquivo {URL} foi gerado com todos os ips nomeados em válidos e inválidoS')



main()