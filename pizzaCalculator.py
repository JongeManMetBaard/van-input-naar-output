#Ali, Goutsal
#Pizza calculator

SmallPizza = (input("Hoeveel small pizza wilt u? "))
MediumPizza = (input("Hoeveel medium pizza wilt u? "))
largePizza = (input("Hoeveel large pizza wilt u? "))

small = 8.99
medium = 10.49
large = 12.99

TotaleKostenSmall = small * float(SmallPizza)
TotaleKostenMedium = medium * float(MediumPizza)
TotaleKostenlarge = large * float(largePizza)

print("U heeft " + str(SmallPizza) + " pizza bestelt en daarvoor betaalt u " + "€" + str(TotaleKostenSmall))
print("U heeft " + str(MediumPizza) + " pizza bestelt en daarvoor betaalt u " + "€" + str(TotaleKostenMedium))
print("U heeft " + str(largePizza) + " pizza bestelt en daarvoor betaalt u " + "€" + str(TotaleKostenlarge))