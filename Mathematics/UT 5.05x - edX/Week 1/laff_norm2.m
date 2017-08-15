function [ alpha ] = laff_norm2( x )
    % performs dot product with itself
    alpha = laff_dot(x, x);
    
    % if dot product failed, return that error
    if(alpha == 'FAILED')
        return
    end
    
    alpha = sqrt(alpha);

end