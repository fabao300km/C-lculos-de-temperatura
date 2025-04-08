# Foi criada uma lista de terperatura para aferição dos dados  
temperaturas = [23.6, 37.9, 25.1, 19.0, 29.8]

# a) Função mim para verificar a menor temperatura 
menor_temperatura = min(temperaturas)

# b) Função max para verificar a maior temperatura
maior_temperatura = max(temperaturas)

# c) Função média para verificar a temperatura média, "sum" para soma todos os valores da lista e "len" para contar o número de elementos da lista
media_temperatura = sum(temperaturas) / len(temperaturas)

# Exibindo os resultados
print(f"Menor temperatura: {menor_temperatura}°C")
print(f"Maior temperatura: {maior_temperatura}°C")
print(f"Temperatura média: {media_temperatura:.2f}°C")
