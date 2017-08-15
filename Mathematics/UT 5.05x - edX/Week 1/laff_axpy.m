function [ y_out ] = laff_axpy( a, x, y )
% laff_axpy takes a scalar 'a' , and two vectors, 
% scales the first one 'a' times, sums it to
% the second one, and returns the result.

    % get sizes of a, x, y
    [a_cols, a_rows] = size(a);
    [x_cols, x_rows] = size(x);
    [y_cols, y_rows] = size(y);

    % check if x and y are vectors, and 'a' a scalar
        % a -> scalar
        if (a_cols ~= 1 || a_rows ~= 1)
            y_out = 'FAILED';
            return
        end
        
        % x, y -> vector
        if (x_cols ~= 1 && x_rows ~=1 || y_cols ~= 1 && y_rows ~=1)
            y_out = 'FAILED';
            return
        end

    % check if x and y have same size
        if(x_cols *  x_rows ~= y_cols * y_rows)
            y_out = 'FAILED';
            return
        end
    
    % create v_size (size of both vectors)
    v_size = x_cols;
    if(v_size < x_rows)
        v_size = x_rows;
    end
    
    % if y is a row vector
    if (y_rows == 1)
        y_out = zeros(v_size, 1);
        for i = 1:v_size
            y_out(i) = y(i) + x(i)*a;
        end
        return
    end
    
    % if y is a column vector
    if(y_cols == 1)
        y_out = zeros(1, v_size);
        for i = 1:v_size
            y_out(i) = y(i) + x(i)*a;
        end
        return
    end

end