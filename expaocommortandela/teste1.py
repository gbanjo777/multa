import pygame
import random

# Inicializa o Pygame
pygame.init()

# Configurações da tela
LARGURA, ALTURA = 800, 600
tela = pygame.display.set_mode((LARGURA, ALTURA))
pygame.display.set_caption("Space Runner")

# Cores
BRANCO = (255, 255, 255)
VERMELHO = (255, 0, 0)
AZUL = (0, 0, 255)

# Carregar imagens
nave_img = pygame.image.load("nave.png")
asteroide_img = pygame.image.load("asteroide.png")
estrela_img = pygame.image.load("estrela.png")

# Classe do Laser
class Laser:
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, 10, 5)
        self.velocidade = 10

    def mover(self):
        self.rect.x += self.velocidade

    def desenhar(self):
        pygame.draw.rect(tela, VERMELHO, self.rect)

# Classe da Nave
class Nave:
    def __init__(self):
        self.image = pygame.transform.rotate(pygame.transform.scale(nave_img, (60, 60)), -90)
        self.image_invertida = pygame.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect(center=(100, ALTURA // 2))
        self.velocidade = 5
        self.lasers = []

    def mover(self, keys):
        if keys[pygame.K_UP] and self.rect.top > 0:
            self.rect.y -= self.velocidade
        if keys[pygame.K_DOWN] and self.rect.bottom < ALTURA:
            self.rect.y += self.velocidade
        if keys[pygame.K_LEFT] and self.rect.left > 0:
            self.rect.x -= self.velocidade
        if keys[pygame.K_RIGHT] and self.rect.right < LARGURA:
            self.rect.x += self.velocidade

    def atirar(self):
        self.lasers.append(Laser(self.rect.right, self.rect.centery))

    def atualizar_lasers(self):
        for laser in self.lasers:
            laser.mover()
        self.lasers = [laser for laser in self.lasers if laser.rect.x < LARGURA]

    def desenhar(self, virada=False):
        if virada:
            tela.blit(self.image_invertida, self.rect)
        else:
            tela.blit(self.image, self.rect)
        for laser in self.lasers:
            laser.desenhar()

# Classe do Asteroide
class Asteroide:
    def __init__(self):
        self.image = pygame.transform.scale(asteroide_img, (50, 50))
        self.rect = self.image.get_rect(midleft=(LARGURA, random.randint(0, ALTURA)))
        self.velocidade = random.randint(4, 8)

    def mover(self):
        self.rect.x -= self.velocidade

    def desenhar(self):
        tela.blit(self.image, self.rect)

# Classe da Estrela
class Estrela:
    def __init__(self):
        self.image = pygame.transform.scale(estrela_img, (40, 40))
        self.rect = self.image.get_rect(midleft=(LARGURA, random.randint(0, ALTURA)))
        self.velocidade = 5

    def mover(self):
        self.rect.x -= self.velocidade

    def desenhar(self):
        tela.blit(self.image, self.rect)

# Função principal
def main():
    clock = pygame.time.Clock()

    nave = Nave()
    asteroides = []
    estrelas = []

    pontuacao = 0
    fonte = pygame.font.Font(None, 36)

    rodando = True
    while rodando:
        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                rodando = False

        # Movimentação da nave
        keys = pygame.key.get_pressed()
        nave.mover(keys)

        # Disparo manual
        if keys[pygame.K_SPACE]:
            nave.atirar()

        nave.atualizar_lasers()

        # Gerar asteroides e estrelas
        if random.random() < 0.03:
            asteroides.append(Asteroide())
        if random.random() < 0.01:
            estrelas.append(Estrela())

        # Atualizar posição
        for asteroide in asteroides:
            asteroide.mover()
        for estrela in estrelas:
            estrela.mover()

        # Colisão com asteroides
        for laser in nave.lasers[:]:
            for asteroide in asteroides[:]:
                if laser.rect.colliderect(asteroide.rect):
                    nave.lasers.remove(laser)
                    asteroides.remove(asteroide)
                    pontuacao += 20

        for asteroide in asteroides:
            if nave.rect.colliderect(asteroide.rect):
                print("Game Over! Pontuação:", pontuacao)
                rodando = False

        for estrela in estrelas[:]:
            if nave.rect.colliderect(estrela.rect):
                pontuacao += 10
                estrelas.remove(estrela)

        # Remover objetos fora da tela
        asteroides = [a for a in asteroides if a.rect.right > 0]
        estrelas = [e for e in estrelas if e.rect.right > 0]

        # Desenhar tudo
        tela.fill((0, 0, 0))
        nave.desenhar(keys[pygame.K_LEFT])

        for asteroide in asteroides:
            asteroide.desenhar()
        for estrela in estrelas:
            estrela.desenhar()

        texto_pontos = fonte.render(f"Pontos: {pontuacao}", True, BRANCO)
        tela.blit(texto_pontos, (10, 10))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    main()
