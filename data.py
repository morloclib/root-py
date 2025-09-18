import sys
import math

def morloc_packMap (xs):
  d = dict()
  ks, vs = xs
  for (k,v) in zip(ks, vs):
    d[k] = v
  return d

def morloc_unpackMap (d):
  return [list(d.keys()), list(d.values())]


def morloc_packUnit (xs):
  return None

def morloc_unpackUnit (d):
  return 1



def morloc_ifelse(cond, x, y):
    if cond:
        return x
    else:
        return y

def morloc_eq(x, y):
    return x == y

def morloc_le(x, y):
    return x <= y

def morloc_fst(t):
    return t[0]

def morloc_snd(t):
    return t[1]

def morloc_toFst(f, x):
    return (f(x), x)

def morloc_toSnd(f, x):
    return (x, f(x))

def morloc_fst3(t):
    return t[0]

def morloc_snd3(t):
    return t[1]

def morloc_thr3(t):
    return t[2]

def morloc_and(x, y):
    return x and y

def morloc_or(x, y):
    return x or y

def morloc_not(x):
    return (not x)

def morloc_neg(x):
    return (-1) * x

def morloc_add(x, y):
    return x + y

def morloc_sub(x, y):
    return x - y

def morloc_inv(x):
    return 1 / x

def morloc_mul(x, y):
    return x * y

def morloc_div(x, y):
    return x / y

def morloc_exp(x, y):
    return x ** y

def morloc_exp(x, y):
    return x ** y

def morloc_log(x, base):
    return math.log(x, base)

#  fold f a b :: (b -> a -> b) -> b -> f a -> b
def morloc_fold(fbab, b, fa):
    for x in fa:
        b = fbab(b, x)
    return b

def morloc_map_list(f, xs):
    return list(map(f, xs))

def morloc_at(i, xs):
    return xs[i]

def morloc_slice(i, j, xs):
    return xs[i:j]
