import numpy as np


FICO_ERR=10**-4

def fico(bam):
    """
    it calculates fitness and complexity

    :param np.array bamjm: the biadjacency matrix
    
    all-zero columns or rows should be already removed
    """    
    ff0=np.sum(bam, axis=1)
    # check that there are no empty rows
    assert 0 not in ff0, 'empty row!'
    qq0=np.sum(bam, axis=0) 
    # check that there are no empty columns
    assert 0 not in qq0, 'empty column!'
    
    c_len, p_len=bam.shape
    ff1=np.ones(c_len)
    qq1=np.ones(p_len)
    ff0=ff0/np.mean(ff0)
    qq0=1./qq0
    qq0=qq0/np.mean(qq0)
 
    while np.sum(abs(ff1-ff0))>FICO_ERR and np.sum(abs(qq1-qq0))>FICO_ERR:
        
        ff0=ff1
        qq0=qq1
        ff1=np.dot(bam, qq0)
        qq1=1./(np.dot(bam.T, 1./ff0))
        ff1/=np.mean(ff1)
        qq1/=np.mean(qq1)
    
    return (ff0, qq0)

def bam_fico_or(bam, return_argsorts=False):
    """
    biadjacency fitness and complexity orderer
    If there are empty rows/columns it can handle it :)
    
    :param np.array bam: the biadjacency to be reordered
    :param bool return_argsorts: choose if you want ba_fico_or to return the 
    argsort for rows and columns, respectively
    
    """
    bam_aux=np.array(bam)
    
    original_shape=bam_aux.shape
    k0=np.sum(bam_aux, axis=1)
    k1=np.sum(bam_aux, axis=0)
    
    bam_aux=bam_aux[k0>0,:]
    bam_aux=bam_aux[:, k1>0]
    
    deg0, deg1=fico(bam_aux)
    no0=np.argsort(-deg0)
    no1=np.argsort(deg1)
    bamno=bam_aux[no0]
    bamno=bamno[:,no1]
    
    if bamno.shape!=original_shape:
        # handling the cases of empty rows/columns
        out=np.zeros(original_shape, dtype=int)
        out[:bamno.shape[0], :bamno.shape[1]]=bamno
        if return_argsorts:
            # put the the right place for the empty rows and columns
            argsort_0=np.zeros(original_shape[0], dtype=int)
            argsort_1=np.zeros(original_shape[1], dtype=int)
            
            # update argsort: rows
            index=0
            index0=len(no0)
            for i in range(original_shape[0]):
                if k0[i]>0:
                    argsort_0[i]=no0[index]
                    index+=1
                else:
                    argsort_0[i]=index0
                    index0+=1
            # update argsort: columns       
            index=0
            index0=len(no1)
            for i in range(original_shape[1]):
                if k1[i]>0:
                    argsort_1[i]=no1[index]
                    index+=1
                else:
                    argsort_1[i]=index0
                    index0+=1
            return out, argsort_0, argsort_1
        else:
            return out
    else:
        if return_argsorts:        
            return bamno, no0, no1
        else:
            return bamno
