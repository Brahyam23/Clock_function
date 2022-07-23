def reloj (*segundos):
    if len(segundos) == 1:
        seg = segundos[0] % 60
        min = (segundos[0] // 60) % 60
        hora= segundos[0] // 3600
        
        print(f"{hora}H:{min}M:{seg}S")
    
    elif len(segundos) ==3:
        seg = (segundos[0] * 3600 + segundos[1] * 60 + segundos[2]) 
        print(f"{seg}S")
    
    else:
        print("Debe ingresar un o tres parámetros unicamente")

reloj(1,30,0)