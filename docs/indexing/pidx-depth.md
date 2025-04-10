## Equivalency by `max-depth` expression

**Author:**: Luke Yoo &lt;[w.lukeyoo@gmail.com](mailto:w.lukeyoo@gmail.com)&gt;
**Date:**: 2025-03-26
**Status**: Draft

In metadata, `depth: 1` is treated the same as not having any metadata.
Therefore, the two following index files are equivalent.

```yaml filename='.pidx'
---
indexee: 'foo/hello-world.md'
title: How we like to greet to the world
date-published: 2025-01-23
author:
    - name: Luke Yoo
    - email: w.lukeyoo@gmail.com
    - website1: https://github.com/micttyoid
tags:
    - Hello
    - World
foo: 42
bar: 'quix'
---
indexee: 'foo/hello-world.md'
title: Cómo nos gusta saludar al mundo
date-published: 2025-03-21
author:
    - name: Luke Yoo
    - email: w.lukeyoo@gmail.com
    - website1: https://github.com/micttyoid
tags:
    - Hola
    - Mundo
foo: 42
bar: 'quix'
---
```



```yaml filename='.pidx'
depth: 1
---
indexee: 'foo/hello-world.md'
title: How we like to greet to the world
date-published: 2025-01-23
author:
    - name: Luke Yoo
    - email: w.lukeyoo@gmail.com
    - website1: https://github.com/micttyoid
tags:
    - Hello
    - World
foo: 42
bar: 'quix'
---
indexee: 'foo/hello-world.md'
title: Cómo nos gusta saludar al mundo
date-published: 2025-03-21
author:
    - name: Luke Yoo
    - email: w.lukeyoo@gmail.com
    - website1: https://github.com/micttyoid
tags:
    - Hola
    - Mundo
foo: 42
bar: 'quix'
---
```