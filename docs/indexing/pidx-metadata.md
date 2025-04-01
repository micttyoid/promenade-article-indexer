# Meta data and comment in index file

**Author:**: Luke Yoo &lt;[w.lukeyoo@gmail.com](mailto:w.lukeyoo@gmail.com)&gt;
**Date:**: 2025-03-31
**Status**: Draft

The two following index files are valid. One without metadata, One with metadata

NOT start with document seperator(no meta)

```yaml
---
indexee: 'foo/hello-world.md'
title: 'How we like to greet to the world'
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
title: 'Cómo nos gusta saludar al mundo'
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

START WITH document separator(metadata)

**No key "indexee" allowed** in the metadata document

```yaml
# Meta Data here. still in YAML
# No key 'indexee' allowed
---
indexee: 'foo/hello-world.md'
title: 'How we like to greet to the world'
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
title: 'Cómo nos gusta saludar al mundo'
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
