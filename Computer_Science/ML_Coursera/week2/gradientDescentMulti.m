function [theta, J_history] = gradientDescentMulti(X, y, theta, alpha, num_iters)
%GRADIENTDESCENTMULTI Performs gradient descent to learn theta
%   theta = GRADIENTDESCENTMULTI(x, y, theta, alpha, num_iters) updates theta by
%   taking num_iters gradient steps with learning rate alpha

% Initialize some useful values
m = length(y); % number of training examples
J_history = zeros(num_iters, 1);

for iter = 1:num_iters
    error = X*theta-y; % diff between predicted value with current theta, and y
    for j = 1:length(theta)
        % update each theta with each feature
        theta(j) = theta(j)-(alpha* sum(error .* X(:, j)))/m;
    end
    % Save the cost J in every iteration    
    J_history(iter) = computeCost(X, y, theta);
end

end
