def Prim(graph):
  """Prim algorithm for minimum spanning tree problem."""
  def AddEdgeToTree(edge, tree):
    f, t = edge
    if f in tree:
      tree[f].append((t, weight))
    else:
      tree[f] = [(t, weight)]
    if t in tree:
      tree[t].append((f, weight))
    else:
      tree[t] = [(f, weight)]
  # END def AddEdgeToTree(edge, tree):
  tree = {0: []}
  while len(tree) < len(graph):
    edge, weight = None, -1
    for t in tree:
      for vw in graph[t]:
        v, w = vw
        if v not in tree and (w < weight or weight < 0):
          edge, weight = (t, v), w
    AddEdgeToTree(edge, tree)
  return tree


def SumOfWeights(g):
  s = 0
  for k,v in g.iteritems():
    for t in v:
      s += t[1]
  return s/2


data = open('p107_network.txt')
graph = {}
i = 0
for line in data:
  line = line.strip()
  if not line:
    continue
  graph[i] = []
  tok = line.split(',')
  for j in range(len(tok)):
    if tok[j] == '-':
      continue
    graph[i].append((j, int(tok[j])))
  i += 1

tree = Prim(graph)
print SumOfWeights(graph) - SumOfWeights(tree)
