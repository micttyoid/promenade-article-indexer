# Promenade Extended Markdown Format Specification

**Author:** Luke Yoo &lt;[w.lukeyoo@gmail.com](mailto:w.lukeyoo@gmail.com)&gt;
**Version:** 0.2.2
**Date:** 2025-03-31

> Markdown + _YAML_ Metadata

## Table of Contents

1. [Overview](#overview)
2. [File Structure](#file-structure)
3. [YAML Metadata Block](#yaml-metadata-block)
4. [Markdown Content](#markdown-content)
5. [Parsing Rule](#parsing-rule)
6. [Examples](#examples)
7. [Compatibility](#compatibility)

## 1. Overview

The format combines standard markdown syntax with optional _YAML_ metadata
blocks, following the pattern established by many modern markdown processors
(sometimes called "front matter" or "frontmatter"). The document consists of two optional
parts:

-   A _YAML_ metadata section
-   A standard markdown content section

## 2. File Structure

```yaml
---
# YAML metadata block (optional)
key: value
another_key: another_value
---
# Standard markdown content follows
# ... follow CommonMark
# ... may follow GitHub Markdown
```

## 3. YAML Metadata Block

-   Must be the first element in the file (optional)
-   Begins and ends with `---` on separate lines
-   Contains valid _YAML 1.2_ between the delimiters
-   Parsed according to _YAML 1.2_ specification
-   Typically used for document attributes like title, author, date, tags, etc.

**See Also:**

-   [2.2. Structures, _YAML 1.2_](https://yaml.org/spec/1.2.2/#22-structures) – separate directives from document content
-   [Front Matter, Jekyll](https://jekyllrb.com/docs/front-matter/) – Metadata format reference

## 4. Markdown Content

Follows the [CommonMark specification](https://commonmark.org/).

May follow _GitHub_ Markdown extension.

All standard markdown features are supported.

Processing begins immediately after the closing `---` of the metadata block (or at start of file if no frontmatter).

## 5. Parsing Rules

1. If the document begins with `---` on the first line(5.a):

    - Parse as _YAML_ until the next `---` on its own line
    - The remaining content is markdown

2. If no opening `---` is present:
    - The entire document is processed as markdown
    - Blank lines around the _YAML_ block are ignored

### 5.a. Parsing Frontmatter

The parsing can be expressed in regular expression:
- _Javascript_: `/^(---|\+\+\+)$[^]*?^\1$(\r\n|\r|\n)/m`


## 6. Examples

Minimal document with no metadata(just markdown):

```yaml
# Foo

Cras sollicitudin erat eget est hendrerit, ut ullamcorper velit sodales. Sed
vulputate tortor nisl, ut volutpat augue dapibus egestas. Praesent non ex
libero. Nam porttitor cursus ligula. Mauris aliquet tempus egestas. Nulla at
sodales ante, quis imperdiet nulla.

## Bar

Vivamus ac pellentesque odio. Aenean porta neque ultrices, mattis nunc quis,
bibendum tortor. Sed tincidunt mauris sed aliquam pharetra.

## Baz

ligula dui dignissim dui, ut viverra neque lorem sed mi. Aliquam a nunc ac
quam consectetur fermentum nec non lectus.
```

Document with metadata:

```yaml
---
title: 'Sample Document'
author: Jane Doe
date: 2023-10-01
tags: [sample, documentation]
---

# Foo

Cras sollicitudin erat eget est hendrerit, ut ullamcorper velit sodales. Sed
vulputate tortor nisl, ut volutpat augue dapibus egestas. Praesent non ex
libero. Nam porttitor cursus ligula. Mauris aliquet tempus egestas. Nulla at
sodales ante, quis imperdiet nulla.

## Bar

Vivamus ac pellentesque odio. Aenean porta neque ultrices, mattis nunc quis,
bibendum tortor. Sed tincidunt mauris sed aliquam pharetra.

## Baz

ligula dui dignissim dui, ut viverra neque lorem sed mi. Aliquam a nunc 
ac quam consectetur fermentum nec non lectus.
```

## 7. Compatibility

Fully backward compatible with standard markdown files

Files without _YAML_ front matter should be processed as normal markdown

_YAML_ parsing should be lenient(ignore unsupported fields but preserve them)

## \_

This specification clarifies:

-   It's standard markdown first and foremost
-   _YAML_ metadata is an optional addition
-   How the two parts relate to each other
-   The exact syntax requirements
