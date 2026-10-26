import gc
print("Grabage collector enabaled", gc.isenabled())
collected = gc.collect()
print("Objects collected:", collected)