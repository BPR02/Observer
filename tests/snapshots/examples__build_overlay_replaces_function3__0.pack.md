# Lectern snapshot

## Data pack

`@data_pack pack.mcmeta`

```json
{
  "pack": {
    "pack_format": 57,
    "description": "",
    "supported_formats": [
      48,
      57
    ]
  },
  "overlays": {
    "entries": [
      {
        "formats": 48,
        "directory": "overlay_48"
      }
    ]
  }
}
```

### demo

`@function demo:demo`

```mcfunction
say this remains in the normal data folder
```

`@function demo:demo2`

```mcfunction
say this remains in the normal data folder (2)
```

`@function demo:demo3`

```mcfunction
say this remains in the normal data folder (3)
```

`@function demo:foo`

```mcfunction
say this is the same in both
```

`@function demo:foo2`

```mcfunction
say this is the same in both (2)
```

`@function demo:nested/demo4`

```mcfunction
say this remains in the normal data folder (4)
```

`@function demo:nested/demo5`

```mcfunction
say this remains in the normal data folder (5)
```

`@function demo:nested/demo6`

```mcfunction
say this remains in the normal data folder (6)
```

`@function demo:nested/foo3`

```mcfunction
say this is the same in both (3)
```

`@function demo:nested/foo4`

```mcfunction
say this is the same in both (4)
```

## Overlay `overlay_48`

`@overlay overlay_48`

### demo

`@function demo:demo`

```mcfunction
say an overlay is created for this
```

`@function demo:demo2`

```mcfunction
say an overlay is created for this (2)
```

`@function demo:demo3`

```mcfunction
say an overlay is created for this (3)
```

`@function demo:nested/demo4`

```mcfunction
say an overlay is created for this (4)
```

`@function demo:nested/demo5`

```mcfunction
say an overlay is created for this (5)
```

`@function demo:nested/demo6`

```mcfunction
say an overlay is created for this (6)
```

`@endoverlay`
