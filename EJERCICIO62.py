# Ejercicio 62

# Tabla de descuento.

# Un supermercado esta ofreciendo el 60% de descuento en una variedad de productos descontinuados 
# el supermercado quiere ayudar a sus clientes a determinar el precio reducido de su mercancia con una
# tabla impresa en los aparadores donde muestre los precios originales y los precios despues de aplicarse
# el descuento. Escribe un programa que use un ciclo while para generar esta tabla mostrando el precio 
# original, el descuento y el nuevo precio para los productos de $4.95, $9,95, $14.95, $24.95. Los descuentos 
# y los nuevos precios deben de ser redondeados a dos decimales.

a = 4.95
print('\n' '|  PRECIO ORIGINAL   |     DESCUENTO    |   PRECIO FINAL   |')  
while a <= 24.95:
    descuento = a * 0.60
    preciof = a - descuento 

    print('____________________________________________________________')
    
    print('|' '\t',a,'\t     ' '|','\t  ' ,'%0.2f' % descuento,'\t'  '|      ','%0.2f' % preciof, '      |')
       
    a = a + 5
