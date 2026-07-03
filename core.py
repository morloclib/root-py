import math
import functools

try:
    import numpy as _np
    _HAS_NUMPY = True
except ImportError:
    _HAS_NUMPY = False

def morloc_idpy(x):
    return x

def morloc_size(x):
    return len(x)

# --- Boolean operations ---

def morloc_not(x):
    return not x

def morloc_and(x, y):
    return x and y

def morloc_or(x, y):
    return x or y

# --- Comparison operations ---

# Structural equality returning a single bool. The naked `x == y` returns
# element-wise masks on numpy arrays (and on some array-like records),
# which violates the Eq class contract that `(==)` yields a single Bool.
# Walk both values in lockstep, reducing arrays / lists / tuples / dicts
# to a single bool via shape-and-content comparison.
def morloc_eq(x, y):
    if _HAS_NUMPY and (isinstance(x, _np.ndarray) or isinstance(y, _np.ndarray)):
        xa = _np.asarray(x)
        ya = _np.asarray(y)
        if xa.shape != ya.shape:
            return False
        if xa.dtype == object or ya.dtype == object:
            return all(morloc_eq(xa.flat[i], ya.flat[i]) for i in range(xa.size))
        return bool(_np.array_equal(xa, ya))
    if isinstance(x, (tuple, list)) and isinstance(y, (tuple, list)):
        if len(x) != len(y):
            return False
        return all(morloc_eq(a, b) for a, b in zip(x, y))
    if isinstance(x, dict) and isinstance(y, dict):
        if x.keys() != y.keys():
            return False
        return all(morloc_eq(x[k], y[k]) for k in x)
    result = x == y
    if _HAS_NUMPY and isinstance(result, _np.ndarray):
        return bool(_np.all(result))
    return bool(result)

def morloc_le(x, y):
    return x <= y

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

def morloc_to_index(x):
    # One helper covers every IndexLike instance because Python's int is
    # arbitrary-precision. UInt64 values above Int64::MAX round-trip safely at
    # the Python level; misinterpretation only occurs if they cross into a
    # typed pool (C++/R) under the same wire-level Int64 tag.
    #
    # Returns Optional[int]: None passes through so slicer bounds can be
    # left blank (the desugar emits `(Null :: ?Int64)` for an empty
    # position, and a user expression evaluating to None composes the
    # same way). Non-None values cast to Python int.
    return None if x is None else int(x)

def morloc_at(i, xs):
    # __access_index__ takes ?Int64 to match __to_index__'s return shape,
    # but a Null index has no semantic meaning at runtime -- callers can
    # only reach this with an explicit Optional-typed index expression
    # that resolved to None.
    if i is None:
        raise IndexError("morloc_at: index is Null")
    return xs[i]

def morloc_slice(start, stop, step, xs):
    # Python's slice() handles None for any of start/stop/step and chooses
    # defaults from the step's sign, matching the Sliceable contract.
    if step == 0:
        raise ValueError("slice step cannot be zero")
    return xs[start:stop:step]

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

# half-open interval [a, b), like Python's range and root's slice
def morloc_range(a, b):
    return list(range(a, b))

def morloc_rangeStep(a, b, step):
    return list(range(a, b, step))

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


