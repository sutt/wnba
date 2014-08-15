import time
import numpy as np
import scipy as sp
from sklearn import linear_model
from err import Err

class Mod:
	
	@staticmethod
	def LogReg(**kwargs):
		""" required: x, y as data
					  fitrows, testrows, x_cols
					  penalty, C
		    returns: fiterr, testerr,
					 fittime,fitheight,fitwidth, x_cols
					 penalty, C
					                               """
		#required
		xData = kwargs.pop('x')
		yData = kwargs.pop('y')
		
		default_cols = xData.columns.values
		x_cols = kwargs.pop('x_cols', default_cols) # as an array of strings for colnames
		
		default_rows = range(xData.shape[0])
		fitrows = kwargs.pop('fitrows', default_rows)
		testrows = kwargs.pop('testrows', default_rows) # if not specified, test is fit
		
		p = kwargs.pop('penalty','l2')
		c = kwargs.pop('C',1.0)
		d_mod = {'penalty':p,'C':c}
		
		xfit = np.array(xData[x_cols])[fitrows]
		print xfit
		yfit = np.array(yData)[fitrows]
		ytest = np.array(yData)[testrows]
		
		start = time.time()
		mod = linear_model.LogisticRegression(penalty = p, C = c)
		mod.fit(X = xfit, y = yfit)
		end = time.time()
		
		yhat = mod.predict_proba(xData[x_cols])
		yhat = map(lambda x: x[1] ,yhat)
		
		fiterror = Err.err(yfit, [yhat[i] for i in fitrows])
		testerror = Err.err(ytest, [yhat[i] for i in testrows])
		d_err = {'fiterr':fiterror,'testerror':testerror}
		
		fit_time = end - start
		fit_height = len(fitrows)
		fit_width = xData[x_cols].shape[1]
		d_domain = {'fit_time':fit_time,'fit_height':fit_height,'fit_width':fit_width, 'x_cols': x_cols}
		print ('done')
		
		return (d_err,d_domain,d_mod)