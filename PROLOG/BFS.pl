% Graph representation: graph(Node, [Neighbors])
graph(a, [b, c]).
graph(b, [a, d, e]).
graph(c, [a, f]).
graph(d, [b]).
graph(e, [b, f]).
graph(f, [c, e]).

% Queue operations
enqueue(Queue, Element, NewQueue) :-
    append(Queue, [Element], NewQueue).

dequeue([Element | Rest], Element, Rest).

% BFS implementation
bfs(Graph, Start, Goal, Path) :-
    bfs([[Start]], Graph, Goal, ReversePath),
    reverse(ReversePath, Path).

% BFS with queue
bfs([[Goal | Path] | _], _, Goal, [Goal | Path]).
bfs([Path | Paths], Graph, Goal, FinalPath) :-
    extend(Path, NewPaths, Graph),
    append(Paths, NewPaths, UpdatedPaths),
    bfs(UpdatedPaths, Graph, Goal, FinalPath).

extend([Node | Path], NewPaths, Graph) :-
    findall([Neighbor, Node | Path], (graph(Node, Neighbors), member(Neighbor, Neighbors), \+ member(Neighbor, [Node | Path])), NewPaths).

% Example usage
?- bfs(graph, a, f, Path).
