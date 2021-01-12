n = float(input('Me diga a distância em metros que vou lhe dizer quantos centímetros e milímetros essa distância tem: '))
m = n*1000
c = n*100
print('A distância {} tem {:.0f} centímetros e {:.0f} miímetros.'.format(n, c, m))