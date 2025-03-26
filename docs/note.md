## Example: file generation

Before

```
foo/hello-world.md
foo/hola-mundo.md
```

Indexer generates and directory looks follow

```
foo/.pidx
foo/hello-world.md
foo/hola-mundo.md
```

## Example: content

Path of the file 1 `foo/hello-world.md`

```yaml
---
promenade-index: 'foo/hello-world.md'
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
(... some Markdown ...)
```

Path to the file 2 in the same directory `foo/hola-mundo.md`

```yaml
---
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
(... algun Markdown ...)
```

Path to the resultant index file, `foo/.pidx`

```yaml
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
