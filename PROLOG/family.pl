male(jim).
male(bob).
male(tom).
male(peter).
male(pat).


female(pam).
female(liz).
female(ann).


parent(tom,bob).
parent(pam,bob).



mother(X,Y):-parent(X,Y),female(X).
father(X,Y):-parent(X,Y),male(X).
brother(X,Y):-parent(X,Y),male(X).
sister(X,Y):-parent(X,Y),female(Y).
