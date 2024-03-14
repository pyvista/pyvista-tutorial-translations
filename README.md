# translated tutorial for pyvista official tutorial

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](CODE_OF_CONDUCT.md)

This is a project to provide pyvista official tutorial with multiple versions and multiple languages.

## URLs

- Tutorial pages for each languages:

  - https://pyvista.github.io/pyvista-tutorial-ja/

## How to update po files

```
sh ./locale/update.sh
```

After that, you should commit updated po files.

## How to add a language

1. add language to locale/update.sh:

   ```
   - rm -R ja
   - tx pull -l ja
   + rm -R ja de
   + tx pull -l ja,de
   ```

1. update po files

1. commit them
