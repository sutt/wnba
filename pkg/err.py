import scipy as sp

class Err:
	
	@staticmethod
	def mic_check():
		return '1,2'
	
	@staticmethod
	def err(act, pred):
		epsilon = 1e-15
		pred = sp.maximum(epsilon, pred)
		pred = sp.minimum(1-epsilon, pred)
		ll = sum(act*sp.log(pred) + sp.subtract(1,act)*sp.log(sp.subtract(1,pred)))
		ll = ll * -1.0/len(act)
		return ll