import matplotlib
import matplotlib.pyplot as plt

matplotlib.use("pgf")
matplotlib.rcParams.update({
    "pgf.texsystem": "pdflatex",
    'font.family': 'serif',
    'text.usetex': True,
    'pgf.rcfonts': False,
})

# first order, n = 6
line1 = plt.plot([0.001, 0.003, 0.005, 0.01, 0.02], [0.66376991936791, 0.55302425923636, 0.58272608024597, 0.60254664065734, 0.62070520275997], 'r-', label='First Order Model')
# second order, n = 6
line2 = plt.plot([0.001, 0.003, 0.005, 0.01, 0.02], [0.63231810079335, 0.4948707557965, 0.52209844943618, 0.54496893686774, 0.56223203242226], 'b-', label='Second Order Model')

plt.setp(line1, marker='.', markersize=10)
plt.setp(line2, marker='.', markersize=10)
plt.axis([0, 0.025, 0, 1])
plt.legend();

#plt.title('Plot of average error in first order and second order model vs observation frequency')
plt.title('n=6')

plt.xlabel("Observation Frequency")
plt.ylabel("Average Error")

plt.savefig("n=6 plot.pgf")
# plt.show()

plt.clf()

# first order, n = 10
line1 = plt.plot([0.001, 0.003, 0.005, 0.01, 0.02], [0.83005955574905, 0.80309235634652, 0.68692948226873, 0.62378371901855, 0.54041107856814], 'r-', label='First Order Model')
# second order, n = 10
line2 = plt.plot([0.001, 0.003, 0.005, 0.01, 0.02], [0.81296773348471, 0.77575592769442, 0.63646332697287, 0.55947823961713, 0.47051453839786], 'b-', label='Second Order Model')

plt.setp(line1, marker='.', markersize=10)
plt.setp(line2, marker='.', markersize=10)
plt.axis([0, 0.025, 0, 1])
plt.legend();

#plt.title('Plot of average error in first order and second order model vs observation frequency')
plt.title('n=10')

plt.xlabel("Observation Frequency")
plt.ylabel("Average Error")

plt.savefig("n=10 plot.pgf")
# plt.show()

plt.clf()

# first order, n = 15
line1 = plt.plot([0.001, 0.003, 0.005, 0.01, 0.02], [0.91369926486564, 0.78826591410145, 0.72001092428544, 0.68368024053515, 0.64551150131066], 'r-', label='First Order Model')
# second order, n = 15
line2 = plt.plot([0.001, 0.003, 0.005, 0.01, 0.02], [0.90757497483375, 0.75728744772309, 0.67101156689949, 0.64088562297514, 0.59800113027174], 'b-', label='Second Order Model')

plt.setp(line1, marker='.', markersize=10)
plt.setp(line2, marker='.', markersize=10)
plt.axis([0, 0.025, 0, 1])
plt.legend();

#plt.title('Plot of average error in first order and second order model vs observation frequency')
plt.title('n=15')

plt.xlabel("Observation Frequency")
plt.ylabel("Average Error")

plt.savefig("n=15 plot.pgf")
# plt.show()