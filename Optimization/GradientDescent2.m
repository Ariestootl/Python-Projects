%%Steepest Descent Method using 
% Backtrack Line Search with Armijo's Condition
%% Jose Aries De Los Santos
clear
clc
close all
syms x1 x2
%Create Objective Function (Rosenbrock Function)
f1 = 100 * (x2 - x1^2)^2 + (1-x1)^2;
f2 = @(x1,x2) 100 .* (x2 - x1.^2).^2 + (1-x1).^2;
fx = inline(f1);
fobj = @(x) fx(x(:,1),x(:,2));


% Use Built-in gradient to acquire the gradient of the Objective Function
fprime = gradient(f1); G = inline(fprime); fp = @(s) G(s(:,1),s(:,2)); 

% Use Built-in gradient to acquire the Matrix of the Objective Function
H1 = hessian(f1); H2 = inline(H1); fh = @(z) H2(z(:,1),z(:,2));

x0 = [0 0]; %initialize


a = 0.5; p = 0.3; c1 = 1e-4;

%% Steepest Descent Algorithm
iter = 0;
X = [];
while norm(fp(x0)) > 1e-5 && iter<2e+3
    X = [X;x0];
    g = -fp(x0);
    H = fh(x0);
    %%Backtracking Line Search with Armijo's condition
    iter1 = 0;
    while fobj(x0 + a*g) > fobj(x0) + c1*a*fp(x0)'*g
        a = p*a;
        iter1 = iter1+1;
    end
    x = x0+ a.*g';
    x0 =  x;
    iter = iter + 1;
end

fprintf("The global minimum are found at %.1f and %.1f\n", x0(1),x0(2))
fprintf("\nThe global minimum is %4.2f",fobj(x0))

% Plotting
fcontour(f2);
hold on;
scatter(x0(1),x0(2),"filled","r");
legend("$Objective$ $Function$", "$Global$ $Minimum$", "Location","Northeast","Interpreter","LaTex","FontSize",13);
title("$Steepest$ $Descent$ $Method$","Interpreter","LaTex", "FontSize",14)
xlabel("$x$","Interpreter","LaTex","FontSize",13);
ylabel("$y$","Interpreter","LaTex","FontSize",13);