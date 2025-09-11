# Dado un string, comprobar si tiene espacios en blanco, en caso de ser cierto, contar cuantos espacios en blanco tiene
# * "in" es como decir: si hay espacios en blanco dentro o en s, entonces haz lo siguiente
s = "Mi gato mola mucho"
blank = " "
if blank in s:
    print("El string tiene {} espacios en blanco" .format(s.count(blank)))
