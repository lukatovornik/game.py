import pygame

sirina=600
visina=400

class Igralec(pygame.sprite.Sprite):
	def __init__(self,up=pygame.K_UP,down=pygame.K_DOWN,left=pygame.K_LEFT,right=pygame.K_RIGHT,color=(200,0,0)):
		super().__init__()
		self.up = up		
		self.down = down
		self.right = right
		self.left = left
		self.color = color
		self.image= pygame.Surface((50,50))
		self.image.fill(color)
		self.rect = self.image.get_rect()
		self.smeri={
			self.up:False,
			self.down:False,
			self.right:False,
			self.left:False
			
		}
	def oznazi_pritisk(self, smer, status):
		self.smeri[smer]=status

	def update(self):
		if self.smeri[self.down]:
			self.premik(0,5)
		if self.smeri[self.up]:
			self.premik(0,-5)
		if self.smeri[self.left]:
			self.premik(-5,0)
		if  self.smeri[self.right]:
			self.premik(5,0)

	def premik(self, x, y):
		self.rect.x+=x
		self.rect.y+=y
		self.rect.x=max(self.rect.x,0)
		self.rect.y=max(self.rect.y,0)
		self.rect.right=min(self.rect.right,sirina)
		self.rect.bottom=min(self.rect.bottom,visina)

igralec= Igralec(pygame.K_w,pygame.K_s,pygame.K_a,pygame.K_d)
igralec2= Igralec(color=(0,0,255))
igra_skupina=pygame.sprite.Group()
igra_skupina.add(igralec)
igra_skupina.add(igralec2)


ekran= pygame.display.set_mode([sirina,visina])
ura= pygame.time.Clock()

igramo=True

while igramo:
	ura.tick(60)
	for dogodek in pygame.event.get():
		if dogodek.type ==pygame.QUIT:
			igramo=False
		elif dogodek.type==pygame.KEYDOWN:
			igralec.oznazi_pritisk(dogodek.key, True)
			igralec2.oznazi_pritisk(dogodek.key, True)
		elif dogodek.type==pygame.KEYUP:
			igralec.oznazi_pritisk(dogodek.key, False)
			igralec2.oznazi_pritisk(dogodek.key, False)
	
	igra_skupina.update()
	ekran.fill((60,100,15))	#hell'o'kity roza (160,100,105)
	igra_skupina.draw(ekran)
	pygame.display.flip()

pygame.quit()