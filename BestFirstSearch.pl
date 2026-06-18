edge(a,b).
edge(b,c).
edge(c,d).
edge(d,e).

best_first(X,Y):-
    edge(X,Y).

best_first(X,Y):-
    edge(X,Z),
    best_first(Z,Y).