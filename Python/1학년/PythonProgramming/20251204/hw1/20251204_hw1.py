from weapon import axe, sword, bow
from character import hunter, knight
import monster
 
hero = knight(sword)
npc = hunter(bow)
m1 = monster.slime()
m2 = monster.orc()
 
hero.attacks(m1)
npc.attacks(m2)
m3, m4 = m1.split()
m2.bigswing(hero, npc)