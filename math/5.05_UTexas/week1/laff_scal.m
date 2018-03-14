function [ x_out ] = laff_scal( a, x )
% Takes scalar 'a', vector 'x', and returns 
% 'a' times 'x'
    
    % Get x size
    [x_cols, x_rows] = size(x);
    
    % Checks if x is a vector
    if (x_cols ~= 1 && x_rows ~= 1)
        x_out = 'FAILED';
        return
    end
    
    % Get alpha size (it must be 1 x 1)
    [a_cols, a_rows] = size(a);
    
    % Checks if a is a scalar
    if(a_cols ~= 1 || a_rows ~= 1)
        x_out = 'FAILED';
        return
    end
    
    % If vector x is a column vector
    if(x_cols == 1)
        x_out = zeros(1, x_rows);
        for i=1:x_rows
            x_out (1, i) = a * x(1, i);
        end
        return
    end
    
    % If vector x is a row vector
    if(x_rows == 1)
        x_out = zeros(x_rows, 1);
        for i=1:x_cols
            x_out (i, 1) = a * x(i, 1);
        end
        return
    end
    return
end