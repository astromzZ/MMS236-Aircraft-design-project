import numpy as np
from collections import defaultdict
v=np.array([[float(k) for k in line.split()[1:]] for line in open('engine.stl') if line.strip().startswith('vertex')]); t=v.reshape(-1,3,3)
print('bounds',v.min(axis=0),v.max(axis=0))
# Analyse one engine; bilateral symmetry means the other is identical.
t=t[np.all(t[:,:,1]>0,axis=1)]
def contours(x):
 seg=[]
 for tri in t:
  if not tri[:,0].min()<x<tri[:,0].max():continue
  hits=[]
  for a,b in [(tri[0],tri[1]),(tri[1],tri[2]),(tri[2],tri[0])]:
   if (a[0]-x)*(b[0]-x)<0:
    c=a+(b-a)*(x-a[0])/(b[0]-a[0]);hits.append(tuple(np.round(c[1:],7)))
  if len(hits)==2:seg.append(hits)
 adj=defaultdict(list)
 for a,b in seg:adj[a].append(b);adj[b].append(a)
 loops=[]
 while adj:
  start=next(iter(adj)); path=[start];last=None;cur=start
  for _ in range(len(seg)+2):
   opts=adj[cur]; nxt=next((q for q in opts if q!=last),None)
   if nxt is None:break
   last,cur=cur,nxt
   if cur==start:break
   path.append(cur)
  for q in path:adj.pop(q,None)
  a=np.array(path)
  area=abs(np.sum(a[:,0]*np.roll(a[:,1],-1)-a[:,1]*np.roll(a[:,0],-1)))/2
  loops.append((area,a))
 return sorted(loops,key=lambda q:q[0],reverse=True)
for x in [31.33,31.4,32,33,33.37321887,34,35,35.7]:
 loops=contours(x);areas=[q[0] for q in loops];print('x',x,'one-engine loops',areas,'pair material',2*(areas[0]-sum(areas[1:])) if areas else 0)
np.save('engine_vertices.npy',v)
