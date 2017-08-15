% First implementation of laff_copy, function that 
% takes two vectors as input. Is meant to be used 
% like: y = laff_copy (x, y).
% Copies vectors from -> to:
% row -> row, col -> col, row -> col, col -> row

function [ y_out ] = laff_copy( x, y )
    
    % get array dimensions    
    [x_cols, x_rows] = size(x);    
    [y_cols, y_rows] = size(y);
    
    % checks if x and y are vectors
    % An array is vector iff has only one dimension
    if (~(x_cols == 1) && ~(x_rows ==1) || ~(y_cols == 1) && ~(y_rows ==1))
        error ('X and Y must be vectors')
        return
    end
    
    % if x and y are column vectors
    % and if x and y have same size
    if(x_cols == 1 && y_cols == 1 && x_rows == y_rows)
        % preallocating y_out
        y_out = zeros(1, x_cols);
        % copying every element of x to y
        for i = 1:x_rows
            y_out ( 1, i ) = x (1, i);
        end        
        return
    end
    
    % if x and y are row vectors
    % and if x and y have same size
    if(x_rows == 1 && y_rows == 1 && x_cols == y_cols)
        % preallocating y_out
        y_out = zeros(x_rows, 1);
        % copying every element of x to y
        for i = 1:x_cols
            y_out ( i, 1 ) = x ( i, 1 );
        end
        return
    end
    
    % if x is col vector, y row vector, 
    % and they have the same size
    if(x_cols == 1 && y_rows == 1 && x_rows == y_cols)
        % preallocating y_out
        y_out = zeros(x_rows, 1);
        % copying every element of x to y
        for i = 1: x_rows
            y_out (i, 1) = x(1, i);
        end
        return
    end
    
    % if x is row vector, y col vector,
    % and they have the same size
    if(x_rows == 1 && y_cols == 1 && x_cols == y_rows)
        % preallocating y_out
        y_out = zeros(1, x_cols);
        % copying every element of x to y
        for i = 1: x_cols
            y_out (1, i) = x (i, 1);
        end
        return
    end
    
    % if none of the previous blocks were executed, 
    % it means x and y weren't the same size
    y_out = 'FAILED';
    
end