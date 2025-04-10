# Implications in Indexing Elements

**Author**: Luke Yoo &lt;[w.lukeyoo@gmail.com](mailto:w.lukeyoo@gmail.com)&gt;
**Date**: 2025-03-31
**Status**: Draft

## Overview


## Implication for Index Entry

Following Frontmatter is sufficient to find the Index Entry:

```yaml
---
indexee: 'foo/bar/baz/hello-world.md'
#         ^^^ index entry
title: 'How we like to greet to the world'
date-published: 2025-01-23
author:
- name: Luke Yoo
- email: w.lukeyoo@gmail.com
---
```

In terms of implying the Index Entry, following Indexee is treated equal:

```yaml
---
indexee: '/foo/bar/baz/hello-world.md'
#         ^^^ Leading slash is effectively the same as the one without
title: 'How we like to greet to the world'
```

**Rationale**: A path expression of Indexee has to be absolute to the
Index Entry. When such query-like result leads to the next request for
the target data, the path can be used directly.

