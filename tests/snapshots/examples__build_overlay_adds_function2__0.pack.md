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

`@function demo:foo`

```mcfunction
say this is the same in both
```

`@function demo:foo2`

```mcfunction
say this is the same in both (2)
```

`@function demo:foo3`

```mcfunction
say this is the same in both (3)
```

`@function demo:foo4`

```mcfunction
say this is the same in both (4)
```

## Overlay `overlay_48`

`@overlay overlay_48`

### demo

`@function demo:demo`

```mcfunction
say this only exists in the overlay
```

`@function demo:demo2`

```mcfunction
say this only exists in the overlay (2)
```

`@function demo:demo3`

```mcfunction
say this only exists in the overlay (3)
```

`@function demo:demo4`

```mcfunction
say this only exists in the overlay (4)
```

`@function demo:demo5`

```mcfunction
say this only exists in the overlay (5)
```

`@function demo:demo6`

```mcfunction
say this only exists in the overlay (6)
```

`@endoverlay`