% Facts: Family relationships
parent(john, alice).
parent(john, bob).
parent(alice, charlie).
parent(bob, david).

% Rules: Definitions of parent and ancestor
ancestor(X, Y) :- parent(X, Y).
ancestor(X, Y) :- parent(X, Z), ancestor(Z, Y).

% Backward chaining implementation
query(X) :- ancestor(john, X).
query(X) :- ancestor(alice, X).
query(X) :- ancestor(bob, X).

% Example queries
?- query(charlie).
true.

?- query(david).
true.

?- query(john).
false.

?- query(susan).
false.
