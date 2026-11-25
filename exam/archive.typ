$
  bold(w)_(mu)^T bold(x_i) &= mat(
    w_1 x_1, dots, w_1 x_k;
    dots, dots, dots;
    w_k x_1, dots, w_k x_k
  ) \
  Delta w_(mu) bold(w)_(mu)^T bold(x_i) &= mat(
    Delta w_(mu) w_1 x_1, dots, Delta w_(mu) w_1 x_k;
    dots, dots, dots;
    Delta w_(mu) w_k x_1, dots, Delta w_(mu) w_k x_k
  ) \
  &= mat(
    x_1, dots, x_k;
    dots, dots, dots;
    x_1, dots, x_k
  )
$

This feels off, and I'm not 100% sure how to represent this. The squared one follows a similar process but is more involved because of the squaring. 