import pandas as pd
import numpy as np
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from mpl_toolkits.mplot3d import Axes3D
import matplotlib.pyplot as plt

# Load the data into a pandas dataframe
data = pd.DataFrame({
    'X': [1880.031, 1895.071, 1910.111, 1925.151, 1940.191, 1955.231, 1970.271, 1985.311, 2000.351, 2015.391, 2030.431, 2045.471, 2060.511, 2075.551, 2090.591, 2105.631, 2120.671, 2135.711, 2150.751, 2165.791, 2180.831, 2195.871, 2210.911, 2225.951, 2240.991, 2256.031, 2271.071, 2286.111, 2301.151, 2316.191, 2331.231, 2346.271, 2361.311, 2376.351, 2391.391, 2406.431, 2421.471, 2436.511],
    'Y': [2256.0255, 2274.0737, 2292.121, 2310.17, 2328.218, 2346.266, 2365.314, 2382.362, 2400.411, 2256.0255, 2274.0737, 2292.121, 2310.17, 2328.218, 2346.266, 2365.314, 2382.362, 2400.411, 2256.0255, 2400.411, 2256.0255, 2274.0737, 2292.121, 2310.17, 2328.218, 2346.266, 2256.0255, 2274.0737, 2292.121, 2310.17, 2328.218, 2346.266, 2365.314, 2382.362, 2400.411, 2256.0255, 2274.0737, 2292.121],
    'Z': [5.68443809073067, 5.71127490572263, 5.24712700664292, 5.512474268178, 5.48746013485485, 5.51531870240139, 5.49496527648263, 5.5184692857103, 5.52109652163849, 5.52383675911836, 5.52520361470608, 5.51557897992833, 5.50005335648231, 5.53164648649268, 5.52988353001381, 5.51904881686335, 5.52557153542131, 5.52827821498971, 5.50481980101545, 5.52318313454222, 5.5091043300413, 5.50485812035051, 5.50619042397636, 5.50792578071662, 5.51122433863178, 5.51231751315045, 5.51323479602369, 5.51136419617223, 5.51434865486658, 5.51168360378753, 5.51184940306429, 5.51597870372004, 5.51209561539056, 5.51294363286527, 5.51325226291548, 5.5132684338684, 5.51446593610554, 5.51475399575844]
})

# Extract the X, Y and Z variables from the data
X = data[['X', 'Y']].values
Z = data['Z'].values

# Create polynomial features of degree 2
poly_features = PolynomialFeatures(degree=2)
X_poly = poly_features.fit_transform(X)

# Fit the polynomial regression model
poly_reg = LinearRegression()
poly_reg.fit(X_poly, Z)

# Create a grid of points to plot the surface
x = np.linspace(min(X[:,0]), max(X[:,0]), 50)
y = np.linspace(min(X[:,1]), max(X[:,1]), 50)
X_grid, Y_grid = np.meshgrid(x, y)
Z_grid = poly_reg.predict(poly_features.fit_transform(np.column_stack((X_grid.ravel(), Y_grid.ravel())))).reshape(X_grid.shape)

# Plot the 3D surface
fig = plt.figure(figsize=(8, 8))
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X_grid, Y_grid, Z_grid, cmap='viridis')
ax.set_xlabel('C1')
ax.set_ylabel('C2')
ax.set_zlabel('Time')
ax.view_init(elev=20, azim=-120)

# Show the plot
plt.show()

min_Z = np.min(Z_grid)
min_idx = np.argmin(min_Z)

min_X = x[min_idx]
print("Minimum value of Z:", min_Z)