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
        "formats": 57,
        "directory": "default_overlay"
      }
    ]
  }
}
```

### demo

`@function demo:foo`

```mcfunction
say this is the same in both
```

`@function demo:foo2`

```mcfunction
say this is the same in both (2)
```

`@function demo:nested/foo3`

```mcfunction
say this is the same in both (3)
```

`@function demo:nested/foo4`

```mcfunction
say this is the same in both (4)
```

## Overlay `default_overlay`

`@overlay default_overlay`

### demo

`@function demo:demo`

```mcfunction
say this only exists in the normal data folder
```

`@function demo:demo2`

```mcfunction
say this only exists in the normal data folder (2)
```

`@function demo:demo3`

```mcfunction
say this only exists in the normal data folder (3)
```

`@function demo:nested/demo4`

```mcfunction
say this only exists in the normal data folder (4)
```

`@function demo:nested/demo5`

```mcfunction
say this only exists in the normal data folder (5)
```

`@function demo:nested/demo6`

```mcfunction
say this only exists in the normal data folder (6)
```

`@endoverlay`
