Pentru punctul d avem:

$P(B=1|T=1,D=1) =$ $\frac{P(B=1)P(T=1)P(D=1)P(D=1|B=1,T=1)}{
    \sum_{b\in\{0,1\}}P(B=b)P(T=1|B=b)P(D=1|B=b,T=1)
}$ = $ \frac{0.1 * 0.8 * 0.9 }{0.1 * 0.8 * 0.9 + 0.9*0.3*0.5} = 0.3478$

Pentru cealalta:
$P(X=1|B=0) = \frac{P(X=1,B=0)}{P(B=0)} = 0.09/0.9 = 0.1$