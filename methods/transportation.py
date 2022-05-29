import numpy as np

def balanced_supply_demand(supply, demand, cost):
    s = np.array(supply)
    d = np.array(demand)
    c = np.matrix(cost, dtype=float)
    if s.sum() > d.sum():
        d = np.append(d, s.sum()-d.sum())
        c = np.concatenate((c,np.zeros((len(s),1))), axis=1)
    elif d.sum() > s.sum():
        s = np.append(s, d.sum()-s.sum())
        c = np.concatenate((c,np.zeros((1,len(d)))), axis=0)
    return (s,d,c)

def north_west_corner(supply, demand, cost):
    s,d,c = balanced_supply_demand(supply, demand, cost)
    assign = np.full((len(s),len(d)), -1)
    i,j = (0,0)
    while (-1 in assign):
        a = min(d[j], s[i])
        d[j] = d[j]-a
        s[i] = s[i]-a
        assign[i,j] = a
        if d[j]==0:
            assign[i+1:,j] = 0
            j+=1
        elif s[i]==0:
            assign[i,:] = np.where(assign[i,:]==-1,0,assign[i,:])
            i+=1
    z = (assign.ravel()*c.A1).sum()
    return (assign, z)

def row_min(supply, demand, cost):
    s,d,c = balanced_supply_demand(supply, demand, cost)
    cc = c.copy()
    assign = np.full(c.shape, -1)
    for i, row in enumerate(c):
        while (-1 in assign[i]):
            j = row.argmin()
            a = min(d[j], s[i])
            d[j] = d[j]-a
            s[i] = s[i]-a
            if d[j] == 0:
                assign[:,j] = np.where(assign[:,j]==-1,0,assign[:,j])
            elif s[i] == 0:
                assign[i,:] = np.where(assign[i,:]==-1,0,assign[i,:])
            assign[i,j] = a
            c[i,j] = np.inf
    z = (assign.ravel()*cc.A1).sum()
    return (assign, z)

def col_min(supply, demand, cost):
    s,d,c = balanced_supply_demand(supply, demand, cost)
    cc = c.copy()
    assign = np.full(c.shape, -1)
    for j, col in enumerate(c.T):
        while (-1 in assign[:,j]):
            i = col.argmin()
            a = min(d[j], s[i])
            d[j] = d[j]-a
            s[i] = s[i]-a
            if d[j]==0:
                assign[:,j] = np.where(assign[:,j]==-1,0,assign[:,j])
            elif s[i]==0:
                assign[i,:] = np.where(assign[i,:]==-1,0,assign[i,:])
            assign[i,j] = a
            c[i,j] = np.inf
    z = (assign.ravel()*cc.A1).sum()
    return (assign, z)
    
def least_cost(supply, demand, cost):
    s,d,c = balanced_supply_demand(supply, demand, cost)
    cc = c.copy()
    assign = np.full(c.shape, -1)
    while (-1 in assign):
        i,j = np.unravel_index(c.argmin(), c.shape)
        a = min(d[j], s[i])
        d[j] = d[j]-a
        s[i] = s[i]-a
        if d[j]==0:
            assign[:,j] = np.where(assign[:,j]==-1,0,assign[:,j])
        elif s[i]==0:
            assign[i,:] = np.where(assign[i,:]==-1,0,assign[i,:])
        assign[i,j] = a
        c[i,j] = np.inf
    z = (assign.ravel()*cc.A1).sum()
    return (assign, z)

def vogel(supply, demand, cost):
    s,d,c = balanced_supply_demand(supply, demand, cost)
    cc = c.copy()
    assign = np.full(c.shape, -1)
    n=1
    while (-1 in assign):
        pr = np.array([])
        pc = np.array([])
        for row in c:
            ro = row.copy()
            ro = ro.A1
            ro.sort()
            if any(np.isinf(ro)[:2]):
                pr = np.append(pr,np.nan)
            else:
                pr = np.append(pr,ro[1]-ro[0])
        for col in c.T:
            co = col.copy()
            co = co.A1
            co.sort()
            if any(np.isinf(co)[:2]):
                pc = np.append(pc,np.nan)
            else:
                pc = np.append(pc,co[1]-co[0])
        pr = np.where(np.isnan(pr) | np.isinf(pr),0,pr)
        pc = np.where(np.isnan(pc) | np.isinf(pc),0,pc)
        if np.count_nonzero(np.append(pr,pc))==1:
            while (-1 in assign):
                i,j = np.unravel_index(c.argmin(), c.shape)
                a = min(d[j], s[i])
                d[j] = d[j]-a
                s[i] = s[i]-a
                if d[j]==0:
                    assign[:,j] = np.where(assign[:,j]==-1,0,assign[:,j])
                elif s[i]==0:
                    assign[i,:] = np.where(assign[i,:]==-1,0,assign[i,:])
                assign[i,j] = a
                c[i,j] = np.inf
        elif pr.max() >= pc.max():
            i = pr.argmax()
            j = c[i].argmin()
            a = min(d[j], s[i])
            d[j] = d[j]-a
            s[i] = s[i]-a
            if d[j]==0:
                assign[:,j] = np.where(assign[:,j]==-1,0,assign[:,j])
                c[:,j] = np.inf
            elif s[i]==0:
                assign[i,:] = np.where(assign[i,:]==-1,0,assign[i,:])
                c[i,:] = np.inf
            assign[i,j] = a
            c[i,j] = np.inf
        else:
            j = pc.argmax()
            i = c[:,j].argmin()
            a = min(d[j], s[i])
            d[j] = d[j]-a
            s[i] = s[i]-a
            if d[j]==0:
                assign[:,j] = np.where(assign[:,j]==-1,0,assign[:,j])
                c[:,j] = np.inf
            elif s[i]==0:
                assign[i,:] = np.where(assign[i,:]==-1,0,assign[i,:])
                c[i,:] = np.inf
            assign[i,j] = a
            c[i,j] = np.inf
        n += 1
        if n>1000:
            break
    
    z = (assign.ravel()*cc.A1).sum()
    return (assign, z)
            
