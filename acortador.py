# acortarodr de enlaces
import pyshorteners
link = input ("Introduc tu enlace:")
shortener = pyshorteners.Shortener().tinyurl
short_link = shortener.short(link)
print("\t Enlace Nuevo:", short_link)




