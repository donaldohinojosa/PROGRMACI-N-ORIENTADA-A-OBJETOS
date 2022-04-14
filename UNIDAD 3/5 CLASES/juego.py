class Pelotajuego:
	puntosinicial =10
	resistencia = 5
	niveles = 1
	vidas = 3

	def game_over(self):
		print("Game over")


pelota = Pelotajuego()
print(pelota.puntosinicial)

pelota.puntosinicial = 0
pelota.vidas = 0

if pelota.puntosinicial == 0 and pelota.vidas == 0:
	pelota.game_over()
