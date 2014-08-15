from matplotlib import pyplot as plt
import numpy as np

class MyPlot:

	@staticmethod
	def miccheck():
		return '1,2'
		
	@staticmethod
	def m_by_n(r,c):
		"""fills across then down
		   should be index x[0],x[1] in subplots """
		return map( lambda x: ((x-(x%c))/c, x % c) ,range(0,r*c) )

	@staticmethod
	def all_hist( df, col_list):
		
		""" for df is pandasdf """
		
		max_x = 5
		
		bplt , axs = plt.subplots(nrows = 5, ncols=3, figsize = (20,27))
	
		for i in range(len(col_list)):
			col = col_list[i]
			vals = filter( lambda x: x == x, df[col] )
			mid = np.mean(vals)
			centers = filter( lambda x: (x < (mid*max_x)),vals )
			bins = mid*max_x if mid*max_x < 30 else 30
			j = MyPlot.m_by_n(5,3)[i]
			axs[j[0],j[1]].hist(centers,bins=bins)
			axs[j[0],j[1]].set_title(col)
		
		bplt.show()