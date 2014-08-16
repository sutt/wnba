import csv
import pickle
from operator import itemgetter
import numpy as np

class Cats:

	@staticmethod 
	def mic_check():
		return 'no print'
		
	@staticmethod
	def cat_dict(column, inp, pick_dir):
		
		d = {}
		ind = 0

		with (open(inp)) as f:
		
			reader = csv.reader(f)
			reader.next()
			
			for row in reader:
				for (i,v) in enumerate(row):
					if i == column:

						if d.has_key(v):
							d[v] = ( (d[v])[0], (d[v])[1] + 1)
						else:
							ind += 1
							d.update({v:(i,1)})
							#print i
			
		#sort and order dict to list
		mydl2 = map(lambda x: (x[0], x[1][0], x[1][1]) ,d.items())
		mydl2.sort(key = itemgetter(2), reverse = True)				
		
		summaryd = [(v[0],(i + 1,v[2])) for i,v in enumerate(mydl2)]
		mapd = [(v[0],i + 1) for i,v in enumerate(mydl2)]
			
		#send to pickle
		pickle.dump(summaryd, open(pick_dir + \
					'sum' + str(column) + '.p','w'))
		pickle.dump(mapd, open(pick_dir + \
					'map' + str(column) + '.p','w'))
						
		return summaryd
	
	@staticmethod
	def score_cat(inp_file, out_file,pick_dir, **kwargs):
	
		fout = open(out_file,'w')
		dict_list = []
		max_cat = kwargs.pop('max_cat',0)
		max_flag = False
		if max_cat > 0:
			max_flag = True
		
		with (open(inp_file)) as f:
			
			#column headers
			fout.write(f.readline())
			reader = csv.reader(f)
			reader.next()

			#rows = np.max([i for i,v in enumerate(row)])
			cat_cols = kwargs.pop('cat_cols')#, range(rows))
			print cat_cols
			
			#load dicts
			for i in cat_cols:
				d = {}
				dl = pickle.load(open(pick_dir + 'map' + str(i) + '.p', 'r'))
				for el in dl:
					d[el[0]] = el[1]
				dict_list.append( d )
			
			#iterate
			for row in reader:
				
				myrow = ''
				for i,v in enumerate(row):
					
					if i > 0:
						myrow += ','
					
					if i in cat_cols: 
						dict_ind = cat_cols.index(i)
						score = dict_list[dict_ind][v]
						if max_flag:
							myrow += str(min(max_cat, score))
						else:
							myrow += str(score)
					else:
						myrow += str(v)

				myrow += '\n'
				fout.write(myrow)

		#finish
		fout.close()
		f.close()
		return 1
			
	