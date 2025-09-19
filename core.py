# imports a bit of a problem, the incur a startup cost even if they are not
# used. I need to find a way to minimize this by making them load lazily. Or
# perhaps by "shaking the tree" and/or compiling the code.
import time
import copy

def morloc_zipWith(f, xs, ys):
    return list(map(f, xs, ys))

def morloc_idpy(x):
    return x

def morloc_elem(x, xs):
    return x in xs

def morloc_run(f):
    return f()

def morloc_neg(x):
  return (-1) * x

def morloc_id(x):
  return x

def morloc_at(i, xs):
  return xs[i]

def morloc_ifelse(cond, x, y):
    if cond:
        return(x)
    else:
        return(y)

def morloc_enumerateWith(f, xs):
  for (x,i) in enumerate(xs):
    yield f(x,i)

def morloc_fold(f, b, xs):
  for x in xs:
    b = f(b, x)
  return b

def morloc_add(a,b):
  return a+b

def morloc_sub(a,b):
  return a-b

def morloc_mul(a,b):
  return a*b

def morloc_div(a,b):
  return a/b

def morloc_map(f, *args):
  return list(map(f, *args))

def morloc_append(xs, x):
    xs.append(x)
    return xs

def morloc_filter(f, xs):
    return [x for x in xs if f(x)]

def morloc_fst(x):
  return x[0]

def morloc_snd(x):
  return x[1]

def morloc_thr3(x):
  return x[2]

#  onFst :: (a -> a') -> (a, b) -> (a', b)
def morloc_onFst(f, x):
    return (f(x[0]), x[1])

#  onSnd :: (b -> b') -> (a, b) -> (a, b')
def morloc_onSnd(f, x):
    return (x[0], f(x[1]))

#  concat :: [[a]] -> [a]
def morloc_concat(xss):
    ys = []
    for xs in xss: 
        ys.extend(xs)
    return ys

#  sleep py :: Real -> a -> a
def morloc_sleep(n, a):
    time.sleep(n)
    return a

#  shard py :: Int -> [a] -> [[a]]
def morloc_shard(chunkSize, xs):
    xss = [[]]
    for x in xs:
        if len(xss[-1]) < chunkSize:
            xss[-1].append(x)
        else:
            xss.append([x])
    return xss

#  [a] -> a
def morloc_head(xs):
    if(len(xs) == 0):
        raise ValueError("Empty list in head operation")
    else:
        return xs[0]

# [a]_{n} -> [a]_{n-1}
def morloc_tail(xs):
    if(len(xs) == 0):
        raise ValueError("Empty list in tail operation")
    else:
        return xs[1:]

# [a] -> a
def morloc_last(xs):
    if(len(xs) == 0):
        raise ValueError("Empty list in last operation")
    else:
        return xs[-1]

# i:Int -> [a]_{n>i} -> [a]_{n=i}
def morloc_take(i, xs): 
    return xs[0:i]

# i:Int -> [a]_{n; n>i} -> [a]_{m; m <= n-i}
def morloc_drop(i, xs):
    return xs[i:]

#  [a]_{n>i} -> [a]_{n-i}
def morloc_init(xs):
    if(len(xs) == 0):
        raise ValueError("Empty list in init operation")
    else:
        return xs[0:-1]

#  join py :: [a] -> [a] -> [a]
def morloc_join(xs, ys):
    # this function should not mutate the data
    xsCopy = copy.copy(xs)
    xsCopy.extend(ys)
    return xsCopy

def morloc_filterKey(cond, d):
    return {k:v for (k, v) in d.items() if cond(k)}

def morloc_filterVal(cond, d):
    return {k:v for (k, v) in d.items() if cond(v)}

def morloc_keys(d):
    return list(d.keys())

def morloc_vals(d):
    return list(d.values())

def morloc_gt(x, y):
	return x > y

def morloc_lt(x, y):
	return x < y

def morloc_ge(x, y):
	return x >= y

def morloc_le(x, y):
	return x <= y

def morloc_eq(x, y):
	return x == y

def morloc_ne(x, y):
	return x != y

def morloc_not(x):
	return (not x)

def morloc_and(x, y):
	return (x and y)

def morloc_or(x, y):
	return (x or y)

def morloc_readMap(filename):
    x = dict()
    with open(filename, "r") as f:
        for line in f.readlines():
            (k,v) = line.split("\t")
            x[k.strip()] = v.strip()
        return x

def morloc_seq(a, b):
    return b

def morloc_const(a, b):
    return a
