#Escreva um programa que leia um valor em metros e exiba o valor convertido em centímetros e milímetros

metros = float(input('Informe o valor em metros: '))
km = metros / 1000
hm = metros / 100
dam = metros / 10
dm = metros * 10
cm = metros * 100
mm = metros * 1000

print("{:.1f}m é equivalente à: \n{:.3f}km - Quilômetros \n{:.3f}hm - Hectômetro".format(metros, km, hm))
print("{:.3f}dam - Decâmetros \n{:.0f}dm - Decímetros \n{:.0f}cm - Centímetros".format(dam, dm, cm))
print("{:.0f}mm - Milímetros".format(mm))