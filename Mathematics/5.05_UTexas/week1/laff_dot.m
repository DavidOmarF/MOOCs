function [ alpha ] = laff_dot( x, y )
% laff_dot performs dot product between two vectors
% which is the sum of the products of x(i) * y(i), 
% with i from 1 to n.

    % get sizes of a, x, y
        [x_cols, x_rows] = size(x);
        [y_cols, y_rows] = size(y);

    % check if x and y are vectors
        if (x_cols ~= 1 && x_rows ~=1 || y_cols ~= 1 && y_rows ~=1)
            alpha = 'FAILED';
            return
        end

    % check if x and y have same size
        if(x_cols *  x_rows ~= y_cols * y_rows)
            alpha = 'FAILED';
            return
        end
        
    % create v_size (size of both vectors)
        v_size = x_cols;
        if(v_size < x_rows)
            v_size = x_rows;
        end
     
    % initialize alpha at 0
    alpha = 0;
    
    % add all products between members of vectors to alpha
    for i = 1:v_size
        alpha = alpha + y(i) * x(i);
    end
end