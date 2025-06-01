;;;
{
    "title": "Foo bar",
    "date-published": "2025-05-25",
    "date-drafted": null,
    "date-modified": "2025-05-25",
    "author": [
        {
            "name": "Foo Bar"
        },
        {
            "email": "foo@bar.com"
    ],
    "tags": [
        "Uno",
        "Dos",
        "Tres",
        "Cuatro"
    ]
}
;;;

# Malform: frontmatter body

Date literals are not directly converted from yaml to json

```
YAML                      JSON
----                      ----
2025-05-25  --(same)-->   "2025-05-25"
```

This is a paragraph of text.

*This text is italic.*

**This text is bold.**

1.  First item
2.  Second item

[Link to a website](https://www.example.com)
