import numpy as np 
import simple_python_package_template

def test_age_estimator():
	param = simple_python_package_template.param()
	t0 = simple_python_package_template.age_estimator(param, 0)
	assert np.abs(t0-13.74)<0.01