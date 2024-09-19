import numpy as np

def compute_cost(x, y, w, b):

    """
    Computes the gradient for linear regression
    Args:
      x (ndarray (m,)): Data, m examples
      y (ndarray (m,)): Target values
      w,b (scalar)    : Model parameters
    Returns
      total_cost      : The total Cost calculated from each example
     """

    # Write your code here

    m = len(x)
    predict = w*x + b
    
    total_cost = (1/m)*np.sum((y-predict)**2)

    return total_cost

x_train = np.array([1.0, 2.0])
y_train = np.array([300.0, 500.0])
print(compute_cost(x_train,y_train,200,100))

