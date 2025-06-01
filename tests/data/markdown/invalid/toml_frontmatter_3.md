+++
title = "Foo bar"
date-published = 2025-05-25
date-modified = 2025-05-25
tags = [ "Uno", "Dos", "Tres", "Cuatro" ]

[[]]
name = "Foo Bar"

[[author]]
email = "foo@bar.com"
+++

# Malform: frontmatter body

Date literals are directly converted from yaml to toml

```
YAML                      TOML
----                      ----
2025-05-25  --(same)-->   2025-05-25
```

This is a paragraph of text.

*This text is italic.*

**This text is bold.**

1.  First item
2.  Second item

[Link to a website](https://www.example.com)

## See also

[toml.io](https://toml.io/en/)