e = float(input('Digite um valor em metros: '))
km = e/1000
hm = e/100
dam = e/10
dm = e * 10
cm = e * 100
mm = e * 1000
print('O valor indicado vale {} km {} hm {} dam'.format(km, hm, dam))
print('O valor indicado vale {} dm {} cm {} mm'.format (dm, cm, mm))
