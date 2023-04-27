X = {"A", "K", "Q", "J", 10, 8}
Y = {"червоний", "чорний", "блакитний", "зелений"}

def decart(X,Y):
   return [(a,b) for a in X for b in Y]

print(decart(X,Y))
