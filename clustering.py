#Finds the clustering coefficient given Adjacenecy matrix
 
import itertools

def l(a,i,r):
   	s=[b for b in r if a[i][b]]
	k=len(s)
	if k<2:
		return 0
	return 2.0*sum(map(lambda x:a[x[0]][x[1]],itertools.combinations(s,2)))/k/(k-1)



def clustering(a):
	n=len(a)
	r=range(n)
	clustering_coeff=[]
	for i in range(n):	
		clustering_coeff.append(l(a,i,r))
	#print "Clustering coefficients are:", clustering_coeff
	return clustering_coeff
