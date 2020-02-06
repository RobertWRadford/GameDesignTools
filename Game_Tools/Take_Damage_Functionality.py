stats = {
	"health": 30,
	"health": 30,
	"atk": 6,
	"Def": 2,
}

currentHealth = stats["health"]

def takeDamage(health, damage):
	health = min(max(health - damage, 0), stats["health"])
	return health

def main():
	cHealth = currentHealth
	print(cHealth)
	cHealth = takeDamage(cHealth, stats["atk"])
	print(cHealth)

main()
