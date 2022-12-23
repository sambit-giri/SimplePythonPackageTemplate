import numpy as np 
import SimplePythonPackageTemplate

def test_age_estimator():
	param = SimplePythonPackageTemplate.param()
	t0 = SimplePythonPackageTemplate.age_estimator(param, 0)
	assert np.abs(t0-13.74)<0.01