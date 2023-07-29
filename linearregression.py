import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression

# Data
X = np.array([1880.031, 1895.071, 1910.111, 1925.151, 1940.191, 1955.231, 1970.271, 1985.311]).reshape((-1, 1))
Y = np.array([2256.0255, 2274.0737, 2292.121, 2310.17, 2328.218, 2346.266, 2365.314, 2382.362]).reshape((-1, 1))
Z = np.array([5.68443809073067, 5.71127490572263, 5.24712700664292, 5.512474268178, 5.48746013485485, 5.51531870240139, 5.49496527648263, 5.5184692857103]).reshape((-1, 1))

# Polynomial Regression
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(X)
Y_poly = poly_features.fit_transform(Y)
XY_poly = np.concatenate((X_poly, Y_poly), axis=1)
poly_model = LinearRegression()
poly_model.fit(XY_poly, Z)

# 3D surface plot
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
x_plot = np.linspace(X.min(), X.max(), 100)
y_plot = np.linspace(Y.min(), Y.max(), 100)
X_plot, Y_plot = np.meshgrid(x_plot, y_plot)
XY_plot = np.concatenate((X_plot.reshape((-1, 1)), Y_plot.reshape((-1, 1))), axis=1)
Z_plot = poly_model.predict(poly_features.fit_transform(XY_plot))
ax.plot_surface(X_plot, Y_plot, Z_plot.reshape(X_plot.shape), cmap='coolwarm')
ax.set_xlabel('X')
ax.set_ylabel('Y')
ax.set_zlabel('Z')
plt.show()
