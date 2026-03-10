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

def morloc_fold1(f, xs):
    acc = xs[0]
    for x in xs[1:]:
        acc = f(acc, x)
    return acc

def morloc_safeFold1(f, xs):
    if not xs:
        return None
    acc = xs[0]
    for x in xs[1:]:
        acc = f(acc, x)
    return acc

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

# --- Stack operations ---

def morloc_cons(x, xs):
    return [x] + xs

def morloc_uncons(xs):
    return (xs[0], xs[1:])

# --- Queue operations ---

def morloc_snoc(xs, x):
    return xs + [x]

def morloc_unsnoc(xs):
    return (xs[:-1], xs[-1])

# --- New list operations ---

def morloc_iterate(n, f, x):
    result = []
    for _ in range(n):
        result.append(x)
        x = f(x)
    return result

def morloc_groupBy(eq, xs):
    if not xs:
        return []
    result = []
    group = [xs[0]]
    for i in range(1, len(xs)):
        if eq(xs[i-1], xs[i]):
            group.append(xs[i])
        else:
            result.append(group)
            group = [xs[i]]
    result.append(group)
    return result

def morloc_find(f, xs):
    for x in xs:
        if f(x):
            return x
    return None

def morloc_unique(xs):
    seen = set()
    result = []
    for x in xs:
        if x not in seen:
            seen.add(x)
            result.append(x)
    return result

def morloc_groupSort(xs):
    groups = {}
    order = []
    for k, v in xs:
        if k not in groups:
            groups[k] = []
            order.append(k)
        groups[k].append(v)
    order.sort()
    return [(k, groups[k]) for k in order]

def morloc_range(a, b):
    if a > b:
        return []
    return list(range(a, b + 1))

def morloc_rangeStep(a, b, step):
    if a > b:
        return []
    return list(range(a, b + 1, step))

# --- Readable operations ---

def morloc_read_int(s):
    try:
        return int(s)
    except (ValueError, TypeError):
        return None

def morloc_read_real(s):
    try:
        return float(s)
    except (ValueError, TypeError):
        return None

def morloc_read_str(s):
    return s

def morloc_read_bool(s):
    if s in ("true", "True", "TRUE"):
        return True
    if s in ("false", "False", "FALSE"):
        return False
    return None

# --- Sequence conversions ---
# In Python, all sequence types map to list, so these are identity functions

def morloc_toDeque(xs):
    return list(xs)

def morloc_toVector(xs):
    return list(xs)

def morloc_toArray(xs):
    return list(xs)

