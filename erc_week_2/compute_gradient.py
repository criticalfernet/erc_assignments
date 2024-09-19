import numpy as np

def compute_gradient(x, y, w, b):
    """
    Computes the gradient for linear regression
    Args:
      x (ndarray (m,)): Data, m examples
      y (ndarray (m,)): target values
      w,b (scalar)    : model parameters
    Returns
      dj_dw (scalar): The gradient of the cost w.r.t. the parameters w
      dj_db (scalar): The gradient of the cost w.r.t. the parameter b
     """

    # Number of training examples
    m = x.shape[0]
    dj_dw = 0
    dj_db = 0 

    # Write your code here

    predict = w*x + b
    error = predict - y

    dj_dw = (1/m)*np.sum(error*x)
    dj_db = (1/m)*np.sum(error)

    return dj_dw, dj_db

x_train = np.array([1.0, 2.0])   
y_train = np.array([300.0, 500.0]) 

print(compute_gradient(x_train,y_train,200,100))
