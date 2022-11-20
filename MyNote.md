

# inf

```py

import math

inf = math.inf

```

# enumerate

enumerate(iter [, initial value])

```py

a = [False, True, False, True]
[idx for idx, b in enumerate(a) if b == True]
[1, 3]
[idx for idx, b in enumerate(a, 2) if b == True]
[3, 5]

```