---
title: "X-first search examples"
date-published: 2025-05-23
date-drafted: null
date-modified: null
author:
  - name: 'Luke Yoo'
  - email: w.lukeyoo@gmail.com
  - website1: https://github.com/micttyoid
tags:
  - 'BFS'
  - 'DFS'
  - 'Breadth-first search'
  - 'Depth-first search'
---

# X-first search examples

## Breadth-first search example

```pseudo
BFS(G, s)
    for each vertex u ∈ G.V - {s}
        u.color = WHITE
        u.d = ∞
        u.π = NIL
    s.color = GRAY
    s.d = 0
    s.π = NIL
    Q = ∅
    ENQUEUE(Q, s)
    while Q != ∅:
        u = DEQUEUE(Q)
        for each v ∈ G.Adj[u]:
            if v.color == WHITE:
                v.color = GRAY
                v.d = u.d + 1
                v.π = u
                ENQUEUE(Q, v)
        u.color = BLACK         // blacken as finished
```

## Depth-first search example

> Discover, explore, and finish

```pseudo
DFS(G)
    for each vertex u ∈ G.V
        u.color = WHITE
        u.π = NIL
    time = 0
    for each vertex u ∈ G.V
        if u.color == WHITE
            DFS-VISIT(G, u)

DFS-VISIT(G, u)
    time = time + 1        // u just discovered
    u.d = time
    u.color = GRAY
    for each v ∈ G.Adj[u]  // explore edge (u, v)
        if v.color == WHITE
            v.π = u
            DFS-VISIT(G, v)
    u.color = BLACK        // blacken u as finished
    time = time + 1
    u.f = time
```

## Reference(s)

- T. H. Cormen, C. E. Leiserson, R. L. Rivest and C. Stein, _Introduction to Algorithms_, 3rd ed. Cambridge, MA: The MIT Press, 2009.