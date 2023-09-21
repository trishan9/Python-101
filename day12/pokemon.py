from prettytable import PrettyTable

x = PrettyTable()
x.add_column("Pokemon Name", ["Pikachu", "Raichu", "Pyroar", "Trishan"])
x.add_column("Pokemon Type", ["Electric", "Electric", "Fire", "Ultimate"])
print(x)