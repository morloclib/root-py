import math
import functools

def morloc_idpy(x):
    return x

# --- Boolean operations ---

def morloc_not(x):
    return not x

def morloc_and(x, y):
    return x and y

def morloc_or(x, y):
    return x or y

# --- Comparison operations ---

def morloc_eq(x, y):
    return x == y

def morloc_le(x, y):
    return x <= y

# --- Control flow ---

def morloc_ifelse(cond, x, y):
    if cond:
        return x
    else:
        return y

def morloc_branch(cond, fa, fb, x):
    if cond(x):
        return fa(x)
    else:
        return fb(x)

# --- Arithmetic operations ---

def morloc_neg(x):
    return (-1) * x

def morloc_abs(x):
    return abs(x)

def morloc_add(a, b):
    return a + b

def morloc_sub(a, b):
    return a - b

def morloc_mul(a, b):
    return a * b

def morloc_intdiv(a, b):
    return a // b

def morloc_mod(a, b):
    return a % b

def morloc_inv(x):
    return 1 / x

def morloc_div(a, b):
    return a / b

def morloc_pow(x, y):
    return x ** y

def morloc_ln(x):
    return math.log(x)

# --- Sequence operations ---

def morloc_at(i, xs):
    return xs[i]

def morloc_slice(i, j, xs):
    return xs[i:j]

def morloc_reverse(xs):
    return list(reversed(xs))

def morloc_sort(xs):
    return sorted(xs)

def morloc_sortBy(cmp, xs):
    def cmp_func(a, b):
        if cmp(a, b):
            return -1
        elif cmp(b, a):
            return 1
        else:
            return 0
    return sorted(xs, key=functools.cmp_to_key(cmp_func))

def morloc_filter(f, xs):
    return [x for x in xs if f(x)]

def morloc_map(f, *args):
    return list(map(f, *args))

def morloc_zipWith(f, xs, ys):
    return list(map(f, xs, ys))

def morloc_fold(f, b, xs):
    for x in xs:
        b = f(b, x)
    return b

def morloc_unzip(xs):
    if not xs:
        return ([], [])
    return ([a for a, b in xs], [b for a, b in xs])

def morloc_replicate(n, x):
    return [x] * n

def morloc_takeWhile(f, xs):
    result = []
    for x in xs:
        if not f(x):
            break
        result.append(x)
    return result

def morloc_dropWhile(f, xs):
    dropping = True
    result = []
    for x in xs:
        if dropping and f(x):
            continue
        dropping = False
        result.append(x)
    return result

def morloc_partition(f, xs):
    yes = []
    no = []
    for x in xs:
        if f(x):
            yes.append(x)
        else:
            no.append(x)
    return (yes, no)

def morloc_scanl(f, init, xs):
    result = [init]
    acc = init
    for x in xs:
        acc = f(acc, x)
        result.append(acc)
    return result

def morloc_intersperse(sep, xs):
    result = []
    for i, x in enumerate(xs):
        if i > 0:
            result.append(sep)
        result.append(x)
    return result

def morloc_enumerate(xs):
    return [(i, x) for i, x in enumerate(xs)]

# --- Map operations ---

def morloc_keys(d):
    return list(d.keys())

def morloc_vals(d):
    return list(d.values())

def morloc_lookup(key, m):
    return m[key]

def morloc_insert(key, val, m):
    result = dict(m)
    result[key] = val
    return result

def morloc_delete(key, m):
    result = dict(m)
    result.pop(key, None)
    return result

def morloc_from_list(xs):
    return dict(xs)

def morloc_to_list(m):
    return list(m.items())

def morloc_map_key(f, m):
    return {f(k): v for k, v in m.items()}

def morloc_map_val(f, m):
    return {k: f(v) for k, v in m.items()}

def morloc_filter_map(f, m):
    return {k: v for k, v in m.items() if f(k, v)}
