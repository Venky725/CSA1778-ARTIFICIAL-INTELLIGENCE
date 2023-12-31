sum(0, 0).         % Base case: The sum of numbers from 1 to 0 is 0.
sum(N, Sum) :-     % Recursive case: Sum of numbers from 1 to N is Sum.
    N > 0,         % Ensure N is positive.
    N1 is N - 1,   % Decrement N by 1.
    sum(N1, Sum1), % Recursively find the sum of numbers from 1 to N1.
    Sum is Sum1 + N.
